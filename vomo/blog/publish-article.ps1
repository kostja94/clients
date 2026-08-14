# VOMO article publisher (non-Node.js edition, curl.exe based)
# Usage (Windows 10/11, bundled curl.exe; no Node.js required):
#   .\publish-article.ps1 validate <article.md>
#   .\publish-article.ps1 draft    <article.md>
#   .\publish-article.ps1 publish  --article-id ID --updated-at VALUE
#   .\publish-article.ps1 status   --job-id ID
#
# Prerequisites:
#   1. Environment variables VOMO_CONTENT_API_URL and VOMO_CONTENT_API_TOKEN must be set.
#   2. The default proxy is http://localhost:15236 (local Veee proxy). Override via
#      the HTTPS_PROXY environment variable or edit $script:Proxy below.

$ErrorActionPreference = "Stop"

$script:API_URL  = $env:VOMO_CONTENT_API_URL
$script:API_TOKEN = $env:VOMO_CONTENT_API_TOKEN
$script:SCHEMA_VERSION = 1
$script:Proxy = if ($env:HTTPS_PROXY) { $env:HTTPS_PROXY } else { "http://localhost:15236" }

if (-not $script:API_URL -or -not $script:API_TOKEN) {
    Write-Error "VOMO_CONTENT_API_URL and VOMO_CONTENT_API_TOKEN must be set as environment variables."
    exit 2
}
$script:API_URL = $script:API_URL.TrimEnd("/")

# Invoke curl.exe and return [statusCode, bodyText]
function Invoke-Curl([string[]]$CurlArgs) {
    if ($script:Proxy) { $CurlArgs += @("-x", $script:Proxy) }
    $CurlArgs += @("--max-time", "120", "-w", "`n__STATUS__%{http_code}")
    $raw = & curl.exe @CurlArgs 2>&1
    $code = $LASTEXITCODE
    if ($code -ne 0) { throw "curl failed (exit $code): $($raw -join ' ')" }
    $joined = $raw -join "`n"
    $parts = $joined -split "__STATUS__"
    $status = [int]$parts[$parts.Count - 1]
    $body = $parts[0..($parts.Count - 2)] -join "`n"
    return @{ Status = $status; Body = $body.Trim() }
}

function Invoke-JsonApi([string]$Endpoint, [string]$Method, [string]$JsonBody) {
    $tmp = Join-Path $env:TEMP ("vomo-payload-" + [guid]::NewGuid().ToString("N") + ".json")
    try {
        [System.IO.File]::WriteAllText($tmp, $JsonBody, (New-Object System.Text.UTF8Encoding($false)))
        $curlArgs = @("-s", "-S", "-X", $Method,
            "$($script:API_URL)$Endpoint",
            "-H", "Authorization: Bearer $($script:API_TOKEN)",
            "-H", "Content-Type: application/json",
            "--data-binary", "@$tmp")
        $r = Invoke-Curl $curlArgs
        return $r
    }
    finally {
        Remove-Item $tmp -ErrorAction SilentlyContinue
    }
}

function Get-Sha256([string]$Path) {
    return (Get-FileHash -Algorithm SHA256 -Path $Path).Hash.ToLowerInvariant()
}

function New-JsonPayload($Object) {
    # PowerShell 5.1 ConvertTo-Json expands decorated strings (Get-Content output)
    # into objects with PSPath/ReadCount. Force plain .NET string values first.
    $plain = @{}
    foreach ($key in $Object.Keys) {
        $val = $Object[$key]
        if ($val -is [string]) { $plain[$key] = [string]$val }
        elseif ($val -is [hashtable] -or $val -is [System.Collections.IDictionary]) {
            $child = @{}
            foreach ($ck in $val.Keys) { $child[[string]$ck] = $val[$ck] }
            $plain[$key] = $child
        }
        else { $plain[$key] = $val }
    }
    return ($plain | ConvertTo-Json -Compress)
}

function Invoke-Validate([string]$ArticleFile) {
    $absolute = (Resolve-Path $ArticleFile).Path
    $markdown = [System.IO.File]::ReadAllText($absolute, [System.Text.Encoding]::UTF8)
    $json = New-JsonPayload @{ schemaVersion = $script:SCHEMA_VERSION; markdown = $markdown }
    $r = Invoke-JsonApi "/api/internal/content/articles/validate" "POST" $json
    if ($r.Status -lt 200 -or $r.Status -ge 300) { throw "validate failed HTTP $($r.Status): $($r.Body)" }
    $result = $r.Body | ConvertFrom-Json
    Write-Host "Valid: $($result.metadata.slug)"
    Write-Host "Assets: $($result.requiredAssets.Count)"
    return @{ Absolute = $absolute; Markdown = $markdown; Result = $result }
}

function Invoke-UploadAsset([string]$ArticleDir, $Asset) {
    $local = Join-Path $ArticleDir $Asset.path
    if (-not (Test-Path $local)) { throw "Asset is not a file: $($Asset.path)" }
    $ext = [System.IO.Path]::GetExtension($local).ToLowerInvariant()
    $mime = switch ($ext) {
        ".jpg"  { "image/jpeg" }
        ".jpeg" { "image/jpeg" }
        ".png"  { "image/png" }
        ".webp" { "image/webp" }
        ".avif" { "image/avif" }
        default { throw "Unsupported image extension: $($Asset.path)" }
    }
    $sha = Get-Sha256 $local
    # curl on Windows accepts forward slashes; keep filename for Content-Disposition
    $curlPath = ($local -replace '\\', '/')
    $fileArg = "${curlPath};type=$mime;filename=$(Split-Path $local -Leaf)"
    $curlArgs = @("-s", "-S", "-X", "POST",
        "$($script:API_URL)/api/internal/content/media",
        "-H", "Authorization: Bearer $($script:API_TOKEN)",
        "-F", "schemaVersion=$($script:SCHEMA_VERSION)",
        "-F", "file=@$fileArg",
        "-F", "alt=$($Asset.alt)",
        "-F", "sourcePath=$($Asset.path)",
        "-F", "sha256=$sha")
    $r = Invoke-Curl $curlArgs
    if ($r.Status -lt 200 -or $r.Status -ge 300) { throw "media upload failed HTTP $($r.Status): $($r.Body)" }
    return ($r.Body | ConvertFrom-Json)
}

if ($args.Count -lt 2) {
    Write-Host "Usage: publish-article.ps1 validate|draft <article.md> | publish --article-id ID --updated-at VALUE | status --job-id ID"
    exit 2
}

$command = $args[0]
try {
    if ($command -eq "validate") {
        $v = Invoke-Validate $args[1]
    }
    elseif ($command -eq "draft") {
        $v = Invoke-Validate $args[1]
        $mediaByPath = @{}
        foreach ($asset in $v.Result.requiredAssets) {
            $uploaded = Invoke-UploadAsset (Split-Path $v.Absolute) $asset
            $mediaByPath[$asset.path] = $uploaded.mediaId
            $mark = if ($uploaded.reused) { "reused" } else { "uploaded" }
            Write-Host "$mark $($asset.path) -> mediaId=$($uploaded.mediaId)"
        }
        $json = New-JsonPayload @{ schemaVersion = $script:SCHEMA_VERSION; markdown = [string]$v.Markdown; mediaByPath = $mediaByPath }
        $draft = Invoke-JsonApi "/api/internal/content/articles" "POST" $json
        if ($draft.Status -lt 200 -or $draft.Status -ge 300) { throw "create draft failed HTTP $($draft.Status): $($draft.Body)" }
        $d = $draft.Body | ConvertFrom-Json
        Write-Host "Article ID: $($d.articleId)"
        Write-Host "updatedAt:  $($d.updatedAt)"
        Write-Host "contentHash: $($d.contentHash)"
        Write-Host "Preview:    $($d.previewUrl)"
        Write-Host "URL:        $($d.url)"
        Write-Host "Wait for explicit reviewer approval before publishing."
    }
    elseif ($command -eq "publish") {
        $articleId = $null; $updatedAt = $null
        for ($i = 1; $i -lt $args.Count; $i++) {
            if ($args[$i] -eq "--article-id") { $articleId = $args[$i + 1] }
            if ($args[$i] -eq "--updated-at") { $updatedAt = $args[$i + 1] }
        }
        if (-not $articleId -or -not $updatedAt) { throw "--article-id and --updated-at are required" }
        $json = @{ schemaVersion = $script:SCHEMA_VERSION; expectedUpdatedAt = $updatedAt } | ConvertTo-Json -Compress
        $pub = Invoke-JsonApi "/api/internal/content/articles/$([uri]::EscapeDataString($articleId))/publish" "POST" $json
        if ($pub.Status -lt 200 -or $pub.Status -ge 300) { throw "publish failed HTTP $($pub.Status): $($pub.Body)" }
        $p = $pub.Body | ConvertFrom-Json
        Write-Host "English published: $($p.url)"
        Write-Host "Translation job: $($p.translationJobId)"
    }
    elseif ($command -eq "status") {
        $jobId = $null
        for ($i = 1; $i -lt $args.Count; $i++) {
            if ($args[$i] -eq "--job-id") { $jobId = $args[$i + 1] }
        }
        if (-not $jobId) { throw "--job-id is required" }
        $st = Invoke-JsonApi "/api/internal/content/translation-jobs/$([uri]::EscapeDataString($jobId))" "GET" ""
        if ($st.Status -ne 200) { throw "status failed HTTP $($st.Status): $($st.Body)" }
        $st.Body | ConvertFrom-Json | ConvertTo-Json -Depth 10
    }
    else {
        throw "Unknown command: $command"
    }
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
