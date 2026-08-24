# Internal Links — Inventário + Plano

> 合并自原 `internal-links.md`（清单）和 `internal-links-plan.md`（策略），统一维护。

**Last updated**: 2026-08-08

---

## Como os links internos funcionam

No Nova Scientia, os links internos são gerados dinamicamente pelos componentes React a partir dos campos estruturados no JSON, não como HTML bruto. Os principais mecanismos são:

| Componente | Campo JSON | Gera link para |
|-----------|-----------|----------------|
| `TopicFeaturedProducts` | `items[].slug` | `/products/{slug}` |
| `TopicRecommendedBar` | `relatedProducts[].slug`, `relatedToolCategories[].slug` | `/products/{slug}` ou `/{segment}` |
| `TopicRecommendedBar` | `recommendedTopics[].slug` | `/{slug}` |
| `TopicComparisonTable` | `rows[].cells[]` | Sem link (texto puro) |
| `CompanyLayout` | `known_products[]`, `indexed_products[].slug` | `/products/{slug}` |
| `ProductAlternatives` | `alternatives[].slug` | `/products/{slug}` (se tiver slug) |
| `BreadcrumbNav` | `content.breadcrumbs[]` | Caminho de navegação |

---

## Regras para Links Internos

### O que FAZER

- **Featured Products**: Incluir 3-6 produtos com slug, linkando para `/products/{slug}`
- **Recommended Topics**: Adicionar 2-4 tópicos relacionados ao final da página
- **Related Products Bar**: Incluir 3-6 produtos recomendados
- **Ordem nos Featured Products**: Produto mais relevante / mais conhecido primeiro
- **Descrições**: Máximo 100 caracteres, foco no diferencial do produto para aquele caso de uso
- **Consistência**: Se um produto aparece em Featured, deve ter página no Nova Scientia
- **Diversidade**: Evitar linkar sempre os mesmos 2-3 produtos em todos os tópicos

### O que NÃO FAZER

- **FAQ**: Proibido incluir links nas respostas (dilui o sinal do schema FAQPage)
- **TL;DR**: Sem links nos points (texto puro)
- **Órfãos**: Todo produto com página deve ser linkado de pelo menos 1 tópico
- **Links quebrados**: Verificar que os slugs referenciados realmente existem

---

## Status Atual (2026-08-08)

| Métrica | Valor |
|---------|-------|
| Tópicos com Featured Products | 35 de 35 (100%) ✅ |
| Tópicos com Recommended Topics | 35 de 35 (100%) ✅ |
| Tópicos sem NENHUM link interno | 0 de 35 ✅ |

**Meta atingida**: 35/35 tópicos com 3-6 Featured Products + 2-4 Recommended Topics. Todos os 107 links de featured apontam para slugs validados (0 broken).

> **Histórico**: o plano original (2026-05-18: 14/35 featured, 2/35 recommended, ~20 sem links) foi totalmente implementado. As seções "Inventário Atual" e "Plano de Implementação" abaixo refletem o estado *antes* da implementação e ficam como registro histórico.

---

## Inventário Atual

### Tópicos → Produtos (via Featured Products)

| Tópico | Produtos Linkados |
|--------|------------------|
| `accent-converter` | utell |
| `agent-for-desktop` | claude |
| `ai-agent` | n8n, manus |
| `cli` | claude, gemini, codex, groq, qwen, coderabbit |
| `face-swap` | akool, falcocut, seaart |
| `family-assistant` | heynori |
| `image-generator` | midjourney, stability, ideogram, firefly |
| `interior-design` | collov-ai |
| `interview-assistant` | finalroundai, interviewcoder, lockedinai, parakeet-ai, linkjob |
| `llm` | chatgpt, claude, gemini, deepseek, grok, perplexity, meta, qwen, mistral |
| `music-generator` | suno, udio, acestudio, tempolor, mureka, producer |
| `podcast-generator` | notebooklm |
| `text-to-speech` | elevenlabs |
| `video-generator` | runway |

### Tópicos → Tópicos (via Recommended Topics)

| Tópico Origem | Tópicos Recomendados |
|---------------|---------------------|
| `agent-for-desktop` | ai-agent, cli, llm |
| `family-assistant` | interview-assistant |

### Tópicos → Produtos (via Related Products Bar)

| Tópico | Produtos na Barra Relacionada |
|--------|------------------------------|
| `interview-assistant` | finalroundai, interviewcoder, lockedinai, parakeet-ai, linkjob |

---

## Plano de Implementação

> **Arquivado** (2026-08-08): plano original, já implementado em todos os 35 tópicos. Mantido como registro histórico.

### 🔴 PRIORIDADE 1 — Sem NENHUM link (20 tópicos)

| Tópico | Featured (slugs) | Recommended |
|--------|-----------------|-------------|
| `3d-model-generator` | meshy, tripo3d, krea | 3d-modelling, 3d-scanner, image-generator |
| `3d-modelling` | meshy, tripo3d, krea | 3d-model-generator, 3d-scanner, interior-design |
| `3d-scanner` | meshy, tripo3d | 3d-model-generator, 3d-modelling, virtual-staging |
| `ai-detector` | zerogpt, scribbr, gptzero | llm, chatbot, search-engine |
| `avatar-generator` | heygen, akool, jogg, aragon | image-generator, headshot-generator, video-generator |
| `chatbot` | chatgpt, claude, gemini, character, chatbase, chaton | llm, ai-agent, cli |
| `filmmaking` | runway, kling-ai, clipchamp, higgsfield | video-generator, video-editor, image-generator |
| `headshot-generator` | headshotpro, aragon, betterpic | avatar-generator, image-generator, image-editor |
| `image-editor` | canva, clipdrop, fotor, picsart | image-generator, image-enhancer, image-relighting |
| `image-enhancer` | magnific, topazlabs, remini | image-editor, image-generator, image-relighting |
| `image-relighting` | clipdrop, leonardo-ai, magnific | image-editor, image-enhancer, image-generator |
| `pattern-generator` | midjourney, firefly, canva | image-generator, tattoo-generator, interior-design |
| `search-engine` | perplexity, exa, writesonic | llm, chatbot, ai-agent |
| `tattoo-generator` | patternlook, midjourney | pattern-generator, image-generator, avatar-generator |
| `video-editor` | clipchamp, runway, kapwing, opus | video-generator, video-translator, filmmaking |
| `video-to-video` | runway, kling-ai, pollo-ai, viggle | video-generator, video-editor, filmmaking |
| `video-translator` | falcocut, captions, akool, dubbing-ai | video-generator, video-editor, voice-generator |
| `virtual-staging` | collov-ai, krea | interior-design, 3d-model-generator, image-generator |
| `voice-changer` | voicemod, murf, kits | voice-generator, voice-cloning, text-to-speech |
| `voice-cloning` | elevenlabs, playht, fish-audio, cartesia | voice-generator, voice-changer, text-to-speech |

### 🟡 PRIORIDADE 2 — Já tem algo, mas incompleto

| Tópico | Ação |
|--------|------|
| `ai-agent` | Adicionar Recommended: agent-for-desktop, cli, llm |
| `cli` | Adicionar Recommended: agent-for-desktop, llm, ai-agent |
| `face-swap` | Adicionar Recommended: image-generator, video-generator, avatar-generator |
| `image-generator` | Adicionar Recommended: image-editor, image-enhancer, avatar-generator |
| `interior-design` | Adicionar Recommended: virtual-staging, 3d-model-generator, image-generator |
| `llm` | 9 featured é demais — reduzir para 6, mover os outros para Recommended |
| `music-generator` | Adicionar Recommended: voice-generator, podcast-generator, voice-cloning |
| `podcast-generator` | Adicionar Featured: fliki, notebooklm / Recommended: voice-generator, music-generator, text-to-speech |
| `text-to-speech` | Adicionar Featured: playht, elevenlabs, speechify / Recommended: voice-generator, voice-cloning, podcast-generator |
| `video-generator` | Adicionar Featured: kling-ai, hailuoai, pixverse, runway / Recommended: video-editor, video-translator, filmmaking |
| `voice-generator` | Adicionar Featured: elevenlabs, playht, murf, cartesia / Recommended: voice-cloning, voice-changer, text-to-speech |

---

## Exemplo de Implementação (JSON)

```json
{
  "content": {
    "featuredProducts": {
      "title": "Melhores Ferramentas de Edição de Vídeo com IA",
      "items": [
        {
          "name": "Runway: Edição Profissional com IA",
          "slug": "runway",
          "description": "Plataforma completa de edição de vídeo com IA generativa. Ideal para criadores e estúdios.",
          "image": "/images/products/runway.png"
        },
        {
          "name": "Clipchamp: Editor Acessível da Microsoft",
          "slug": "clipchamp",
          "description": "Editor de vídeo online com IA integrada. Perfeito para iniciantes e equipes.",
          "image": "/images/products/clipchamp.png"
        }
      ]
    },
    "recommendedTopics": [
      { "name": "Geradores de Vídeo com IA", "slug": "video-generator" },
      { "name": "Tradutores de Vídeo com IA", "slug": "video-translator" },
      { "name": "IA para Cinema", "slug": "filmmaking" }
    ]
  }
}
```

> **Nota**: Imagens usam caminhos locais `/images/products/{slug}.png` (migrados do Supabase em 2026-06-06).

---

## Verificação Pós-Implementação

Após adicionar os links a cada tópico, rodar:

```bash
python3 -c "
import json, os
products = {f.replace('.json','') for f in os.listdir('content/products') if f.endswith('.json')}
topics = {f.replace('.json','') for f in os.listdir('content/topics') if f.endswith('.json')}
for f in os.listdir('content/topics'):
    if not f.endswith('.json'): continue
    d = json.load(open(f'content/topics/{f}'))
    for item in d.get('content',{}).get('featuredProducts',{}).get('items',[]):
        if item.get('slug') and item['slug'] not in products:
            print(f'BROKEN: {f} → featured product slug \"{item[\"slug\"]}\" not found')
    for rt in d.get('content',{}).get('recommendedTopics',[]):
        if rt.get('slug') and rt['slug'] not in topics:
            print(f'BROKEN: {f} → recommended topic slug \"{rt[\"slug\"]}\" not found')
"
```

---

## Ordem de Execução Recomendada

> ✅ Executada integralmente (2026-08-08) — todos os tópicos das 4 fases foram implementados.

| Fase | Tópicos |
|------|---------|
| Semana 1 — Alto tráfego | video-generator, image-generator, chatbot, voice-generator, llm |
| Semana 2 — Prioridade 1 | video-editor, video-translator, video-to-video, filmmaking, voice-changer, voice-cloning, search-engine |
| Semana 3 — Prioridade 1 | headshot-generator, avatar-generator, image-editor, image-enhancer, image-relighting, ai-detector, 3d-model-generator, virtual-staging |
| Semana 4 — Nicho | 3d-modelling, 3d-scanner, tattoo-generator, pattern-generator, text-to-speech |
