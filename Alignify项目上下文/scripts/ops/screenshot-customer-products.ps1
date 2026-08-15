<#
.SYNOPSIS
    Firecrawl Screenshot Script for Customer Stories Featured Products (PowerShell)
.DESCRIPTION
    Takes viewport screenshots of 6 featured product homepages using Firecrawl REST API,
    saves them as JPGs to public/assets/customer-stories/.

    Modes:
      Default         Screenshot all 6 products (skips existing)
      -Only KEY       Screenshot a single product by key
      -RetryFailed    Re-screenshot only previously failed products
      -Report         Print summary of existing screenshots
      -Quality N      JPEG quality (default 85)

    Requirements:
      - PowerShell 7+ (for Invoke-RestMethod)
      - Firecrawl API key (embedded below)

.EXAMPLE
    .\screenshot-customer-products.ps1
    .\screenshot-customer-products.ps1 -Only tunee
    .\screenshot-customer-products.ps1 -RetryFailed
    .\screenshot-customer-products.ps1 -Report
    .\screenshot-customer-products.ps1 -Quality 90
#>

param(
    [Parameter(Mandatory = $false)]
    [string]$Only,

    [switch]$RetryFailed,

    [switch]$Report,

    [ValidateRange(1, 100)]
    [int]$Quality = 85
)

# ── Config ──────────────────────────────────────────────────────────

$FIRECRAWL_API_KEY = "fc-6e6e4c926dae4648a65f388b57f1e346"
$FIRECRAWL_URL     = "https://api.firecrawl.dev/v1/scrape"

# Auto-detect project root
$possibleRoots = @(
    "D:\部署项目\alignify-by-kostja",
    "D:\Deploy\alignify-by-kostja"
)
$PROJECT_ROOT = $null
foreach ($p in $possibleRoots) {
    if (Test-Path $p) { $PROJECT_ROOT = $p; break }
}
if (-not $PROJECT_ROOT) {
    $PROJECT_ROOT = Split-Path $PSCommandPath -Parent
}

$OUTPUT_DIR    = Join-Path $PROJECT_ROOT "public\assets\customer-stories"
$SCRIPT_DIR    = Split-Path $PSCommandPath -Parent
$FAILED_CACHE  = Join-Path $SCRIPT_DIR ".failed-cache.json"

$PRODUCTS = @(
    @{ Key = "tunee";      Url = "https://www.tunee.ai/";               Label = "Tunee — Voice / Music" }
    @{ Key = "voispark";   Url = "https://voispark.com/";                Label = "VoiSpark — Voice / TTS" }
    @{ Key = "lessie-ai";  Url = "https://lessie.ai/";                   Label = "Lessie AI — Agent / Growth Intel" }
    @{ Key = "medeo-ai";   Url = "https://www.medeo.app/";               Label = "Medeo AI — Agent / Video" }
    @{ Key = "finalround"; Url = "https://www.finalroundai.com/";         Label = "Final Round AI — Agent / Career" }
    @{ Key = "thetawave";  Url = "https://thetawave.ai/";                Label = "ThetaWave — Industry / EdTech" }
)

# ── Helpers ─────────────────────────────────────────────────────────

function Download-WithRetry {
    param([string]$ScreenshotUrl, [string]$OutputPath, [int]$MaxRetries = 3)

    for ($attempt = 1; $attempt -le $MaxRetries; $attempt++) {
        try {
            $outDir = Split-Path $OutputPath -Parent
            if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

            Invoke-WebRequest -Uri $ScreenshotUrl -OutFile $OutputPath -TimeoutSec 60 -ErrorAction Stop

            $file = Get-Item $OutputPath
            $sizeKB = [math]::Round($file.Length / 1KB)
            Write-Host "    ✓ $OutputPath ($sizeKB KB)" -ForegroundColor Green
            return $true
        }
        catch {
            if ($attempt -lt $MaxRetries) {
                $wait = $attempt * 3
                Write-Host "    ⟳ Retry $attempt/${MaxRetries} after ${wait}s: $($_.Exception.Message)" -ForegroundColor Yellow
                Start-Sleep -Seconds $wait
            } else {
                Write-Host "    ✗ Failed after $MaxRetries attempts: $($_.Exception.Message)" -ForegroundColor Red
            }
        }
    }
    return $false
}


function Invoke-Screenshot {
    param([string]$Url, [string]$OutputPath, [string]$Label, [int]$Quality = 85)

    $headers = @{
        "Content-Type" = "application/json"
        "Authorization" = "Bearer $FIRECRAWL_API_KEY"
    }

    $body = @{
        url = $Url
        formats = @(
            @{
                type     = "screenshot"
                fullPage = $false
                quality  = $Quality
            }
        )
    } | ConvertTo-Json -Depth 5

    try {
        Write-Host "  [$Label]"
        Write-Host "    URL: $Url"

        $response = Invoke-RestMethod -Uri $FIRECRAWL_URL -Method Post -Headers $headers -Body $body -TimeoutSec 90 -ErrorAction Stop

        $screenshotUrl = $response.data.screenshot
        if (-not $screenshotUrl) {
            Write-Host "    ✗ No screenshot in response" -ForegroundColor Red
            return $false
        }

        return Download-WithRetry -ScreenshotUrl $screenshotUrl -OutputPath $OutputPath
    }
    catch {
        Write-Host "    ✗ $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}


function Load-FailedCache {
    if (Test-Path $FAILED_CACHE) {
        try {
            $data = Get-Content $FAILED_CACHE -Raw | ConvertFrom-Json
            return @($data)
        } catch { return @() }
    }
    return @()
}


function Save-FailedCache {
    param([string[]]$Keys)
    try {
        $Keys | ConvertTo-Json | Set-Content $FAILED_CACHE -Encoding utf8
    } catch {
        # best effort
    }
}

# ── Modes ───────────────────────────────────────────────────────────

function Invoke-Default {
    if (-not (Test-Path $OUTPUT_DIR)) { New-Item -ItemType Directory -Path $OUTPUT_DIR -Force | Out-Null }

    $total = $PRODUCTS.Count
    Write-Host "Customer Stories — Featured Product Screenshots" -ForegroundColor Cyan
    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host "Products: $total  |  Quality: $Quality  |  Output: $OUTPUT_DIR"
    Write-Host ("=" * 60)
    Write-Host ""

    $results = @{ Success = 0; Skipped = 0; Failed = 0 }
    $failedKeys = @()

    foreach ($p in $PRODUCTS) {
        $outPath = Join-Path $OUTPUT_DIR "$($p.Key).jpg"

        if (Test-Path $outPath) {
            $file = Get-Item $outPath
            $sizeKB = [math]::Round($file.Length / 1KB)
            Write-Host "  EXISTS ($sizeKB KB): $outPath" -ForegroundColor Gray
            $results.Skipped++
            continue
        }

        $t0 = Get-Date
        $ok = Invoke-Screenshot -Url $p.Url -OutputPath $outPath -Label $p.Label -Quality $Quality
        $elapsed = [math]::Round(((Get-Date) - $t0).TotalSeconds, 1)
        $icon = if ($ok) { "✓" } else { "✗" }
        Write-Host "    $icon  (${elapsed}s)" -ForegroundColor $(if ($ok) { "Green" } else { "Red" })
        Write-Host ""

        if ($ok) { $results.Success++ } else { $results.Failed++; $failedKeys += $p.Key }
    }

    Save-FailedCache -Keys $failedKeys

    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host "Results: $($results.Success) succeeded, $($results.Skipped) skipped, $($results.Failed) failed"
    if ($results.Failed -gt 0) {
        Write-Host "Retry with: .\screenshot-customer-products.ps1 -RetryFailed" -ForegroundColor Yellow
    }
    Write-Host "Done. Images in: $OUTPUT_DIR" -ForegroundColor Green
    return $results.Failed -eq 0
}


function Invoke-RetryFailed {
    $failedKeys = Load-FailedCache
    if ($failedKeys.Count -eq 0) {
        Write-Host "No failed products cached — nothing to retry." -ForegroundColor Green
        return $true
    }

    $targets = $PRODUCTS | Where-Object { $_.Key -in $failedKeys }
    if ($targets.Count -eq 0) {
        Write-Host "No matching products found in cache." -ForegroundColor Yellow
        return $true
    }

    Write-Host "Retrying $($targets.Count) previously failed product(s):" -ForegroundColor Cyan
    foreach ($p in $targets) { Write-Host "  • $($p.Label) ($($p.Url))" }
    Write-Host ""

    $stillFailed = @()
    foreach ($p in $targets) {
        $outPath = Join-Path $OUTPUT_DIR "$($p.Key).jpg"
        $t0 = Get-Date
        $ok = Invoke-Screenshot -Url $p.Url -OutputPath $outPath -Label $p.Label -Quality $Quality
        $elapsed = [math]::Round(((Get-Date) - $t0).TotalSeconds, 1)
        $icon = if ($ok) { "✓" } else { "✗" }
        Write-Host "    $icon  (${elapsed}s)" -ForegroundColor $(if ($ok) { "Green" } else { "Red" })
        Write-Host ""
        if (-not $ok) { $stillFailed += $p.Key }
    }

    Save-FailedCache -Keys $stillFailed

    if ($stillFailed.Count -gt 0) {
        Write-Host "Still failed: $($stillFailed.Count)/$($targets.Count)" -ForegroundColor Red
        Write-Host "Run again with -RetryFailed to retry these." -ForegroundColor Yellow
        return $false
    } else {
        Write-Host "All retried products succeeded!" -ForegroundColor Green
        return $true
    }
}


function Invoke-Only {
    param([string]$Key)

    $match = $PRODUCTS | Where-Object { $_.Key -eq $Key }
    if (-not $match) {
        $available = ($PRODUCTS | ForEach-Object { $_.Key }) -join ", "
        Write-Host "No product found with key: $Key" -ForegroundColor Red
        Write-Host "Available: $available"
        return $false
    }

    $outPath = Join-Path $OUTPUT_DIR "$($match.Key).jpg"
    if (-not (Test-Path $OUTPUT_DIR)) { New-Item -ItemType Directory -Path $OUTPUT_DIR -Force | Out-Null }

    Write-Host "Screenshotting 1 product: $($match.Label)" -ForegroundColor Cyan
    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host ""

    $t0 = Get-Date
    $ok = Invoke-Screenshot -Url $match.Url -OutputPath $outPath -Label $match.Label -Quality $Quality
    $elapsed = [math]::Round(((Get-Date) - $t0).TotalSeconds, 1)
    Write-Host ""
    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host "$(if ($ok) { '✓' } else { '✗' })  (${elapsed}s)" -ForegroundColor $(if ($ok) { "Green" } else { "Red" })
    return $ok
}


function Invoke-Report {
    $existing = @()
    $missing  = @()

    foreach ($p in $PRODUCTS) {
        $path = Join-Path $OUTPUT_DIR "$($p.Key).jpg"
        if (Test-Path $path) {
            $file = Get-Item $path
            $sizeKB = [math]::Round($file.Length / 1KB)
            $ageHours = [math]::Round(((Get-Date) - $file.LastWriteTime).TotalHours, 1)
            $existing += [PSCustomObject]@{
                Label    = $p.Label
                SizeKB   = $sizeKB
                AgeHours = $ageHours
                Key      = $p.Key
            }
        } else {
            $missing += $p
        }
    }

    Write-Host "Customer Stories Screenshot Report" -ForegroundColor Cyan
    Write-Host ("=" * 60)
    Write-Host "Output: $OUTPUT_DIR"
    Write-Host "Total : $($PRODUCTS.Count) products"
    Write-Host "Done  : $($existing.Count)   Missing: $($missing.Count)"
    Write-Host ""

    if ($existing.Count -gt 0) {
        Write-Host "Existing Screenshots:" -ForegroundColor Yellow
        Write-Host ("-" * 60)
        foreach ($e in $existing) {
            $ageStr = if ($e.AgeHours -lt 72) { "$($e.AgeHours)h" } else { "$([math]::Round($e.AgeHours/24, 1))d" }
            Write-Host "  $($e.Label.PadRight(40)) $($e.SizeKB.ToString().PadLeft(5)) KB  $ageStr"
        }
        Write-Host ""
    }

    if ($missing.Count -gt 0) {
        Write-Host "Missing:" -ForegroundColor Red
        foreach ($m in $missing) {
            Write-Host "  $($m.Label) → .\screenshot-customer-products.ps1 -Only $($m.Key)"
        }
        Write-Host ""
    }

    return $missing.Count -eq 0
}

# ── Dispatch ────────────────────────────────────────────────────────

$exitCode = 0
try {
    if ($Report) {
        $ok = Invoke-Report
    } elseif ($RetryFailed) {
        $ok = Invoke-RetryFailed
    } elseif ($Only) {
        $ok = Invoke-Only -Key $Only
    } else {
        $ok = Invoke-Default
    }
    if (-not $ok) { $exitCode = 1 }
}
catch {
    Write-Host "Fatal error: $_" -ForegroundColor Red
    $exitCode = 1
}

exit $exitCode
