# 🤖 CONTEXTO TÉCNICO — ORGANIZADOR DE PRESENTES DO FELIXO

> **O que é**: Memória técnica persistente do projeto para uso por modelos de IA.
> **Baseado em**: Template `IA.md` do Felixo System Design.
> **Regra fundamental**: Todo contexto relevante deve estar neste único arquivo.

---

## 🎯 OBJETIVO DO PROJETO

[2026-04-27] Aplicação web single-file (HTML + CSS + JS puro) para organizar ideias de presentes.  
Público: uso pessoal. Deploy: nenhum — roda localmente ao abrir o `.html` no navegador.  
Prioridade: simplicidade e zero dependências de servidor.

---

## 🏁 METAS & MILESTONES

[2026-04-27] ✅ Concluída — Estrutura base da aplicação (HTML + CSS + JS em arquivo único)  
[2026-04-27] ✅ Concluída — CRUD completo de presentes com localStorage  
[2026-04-27] ✅ Concluída — Exportação e importação via JSON  
[2026-04-27] ✅ Concluída — Sistema de tags, busca e filtros  
[2026-04-27] ✅ Concluída — Botão flutuante (FAB) responsivo  
[2026-04-27] ✅ Concluída — Alinhamento ao Felixo Design System (cores + fonte)  
[2026-04-27] ✅ Concluída — README completo seguindo DESIGN_SYSTEM_PARA_README.md  
[2026-04-27] ✅ Concluída — Deploy no GitHub Pages com domínio customizado gifts.felixo.com.br  
[2026-06-01] ✅ Concluída — Redesign do `index.html` aplicando o Felixo Frontend Design System (paleta zinc/black, glow respirante, partículas roxas, cards do design system)  
[2026-06-01] ✅ Concluída — Acessibilidade: modal com `role="dialog"`/`aria-modal`, fechar com Esc/overlay, restauração de foco, `aria-label` no FAB, labels `sr-only` nos controles  
[2026-06-01] ✅ Concluída — Validação de URL contra XSS (bloqueio de `javascript:`/`data:` em links) e correção do contrato `imageIsURL`  

---

## 🛠️ STACK & DEPENDÊNCIAS

[2026-04-27] Front-end: HTML5 + CSS3 + JavaScript ES6+ vanilla  
[2026-04-27] Fonte: Space Grotesk (Google Fonts) — padrão Felixo Design System  
[2026-04-27] Persistência: localStorage do navegador (chave: `felixo_gifts_v1`)  
[2026-04-27] Sem dependências externas além da fonte — nenhum framework, nenhuma lib JS  

---

## 📐 DECISÕES DE ARQUITETURA

[2026-04-27] Single-file HTML ao invés de projeto multi-arquivo — objetivo é simplicidade máxima; o usuário só precisa de um arquivo para usar.  
[2026-04-27] localStorage como banco de dados — adequado para uso pessoal sem servidor; dados ficam no próprio navegador.  
[2026-04-27] Exportação/importação JSON — mecanismo de backup e portabilidade para compensar a natureza local do storage.  
[2026-04-27] IIFE (immediately invoked function expression) no script — encapsula todo o estado sem poluir o escopo global.  
[2026-04-27] Imagens armazenadas como base64 via FileReader — permite persistir imagens locais sem servidor de upload.  
[2026-04-27] Dados de exemplo inseridos no primeiro uso (`gifts.length === 0`) — melhora onboarding sem tela em branco.  

---

## 🎨 DECISÕES DE DESIGN & CONVENÇÕES

[2026-04-27] Cores alinhadas ao Felixo Design System: `--accent: #A855F7` (Felixo Purple Bright), `--accent-soft: #C084FC` (Felixo Purple estático).  
[2026-04-27] Fonte: `Space Grotesk` via Google Fonts — substituiu Inter para seguir o padrão Felixo.  
[2026-04-27] Gradientes de elementos interativos (logo, FAB, botão primário): `linear-gradient(135deg, #A855F7, #C084FC)`.  
[2026-04-27] Sombra do FAB em hover: `rgba(168,85,247,0.6)` — RGB de `#A855F7`.  
[2026-04-27] Tags: `border-radius: 999px` (pill), fundo sutil `rgba(255,255,255,0.04)`.  
[2026-04-27] Cards com `border-radius: 12-14px`, sombra escura `rgba(2,6,23,0.6)`.  
[2026-06-01] Redesign alinhado ao `felixo-standards/core/DESIGN_SYSTEM_FRONTEND.md`: fundo `linear-gradient(black → zinc-950 → black)` fixo, cards `bg-zinc-950/50` com `border rgba(255,255,255,0.10)` e `border-radius` 1.5rem (rounded-3xl), inputs `rounded-xl` com focus glow roxo (`box-shadow 2px/4px rgba(168,85,247,...)`).  
[2026-06-01] Glow respirante (`card-glow-breathe` 3s ease-in-out) ativado no hover dos cards; título "Felixo" usa `text-felixo-purple-glow` (animação `text-glow-breathe`).  
[2026-06-01] Partículas de fundo: 35 partículas roxas (`#e9d5ff`, glow `rgba(192,132,252,0.8)`) flutuando para cima — geradas em JS, respeitando `prefers-reduced-motion`.  
[2026-06-01] Tags repaginadas para o roxo Felixo (`rgba(168,85,247,0.10)` fundo, `#C084FC` texto). Badge de status "✓ Comprado" em verde (`rgba(34,197,94,...)`) seguindo as cores de status do design system.  
[2026-06-01] Seletor de grade (`#gridCols`): Auto / 2 / 3 / 4 / 5 colunas por linha via atributo `data-cols` no `.grid` (CSS `grid-template-columns:repeat(N,1fr)`). 'auto' remove o override e volta ao `auto-fill minmax(260px,1fr)`. Em ≤900px grade fixa cai para 2 colunas; em ≤560px vira 1 coluna.  
[2026-06-01] Preferência de grade persistida em chave própria `felixo_gifts_prefs_v1` (separada dos dados em `felixo_gifts_v1`) via `loadPrefs`/`savePrefs`.  
[2026-06-01] Presentes comprados: `.gift-card.purchased` com `opacity:0.55` + `grayscale(0.35)` (no hover sobe para `0.85`/`0.1`) — destaque visual de "já comprado" que se perdera no redesign.  

---

## 🧪 TESTES IMPORTANTES

[2026-04-27] ✅ Salvar/editar/apagar presente — ciclo CRUD completo via localStorage funcional.  
[2026-04-27] ✅ Exportar JSON — gera arquivo `.json` com data no nome.  
[2026-04-27] ✅ Importar JSON — mescla dados importados com os existentes; sanitiza campos.  
[2026-04-27] ✅ Upload de imagem via arquivo — converte para base64 e exibe preview em tempo real.  
[2026-04-27] ✅ Busca em tempo real — pesquisa em título, tags e notas simultaneamente.  

---

## 🐛 BUGS & FIXES RELEVANTES

[2026-04-27] Tags inicialmente limitadas a palavras únicas — corrigido para aceitar múltiplas palavras separadas por espaço ou vírgula, usando split `/[\s,]+/`.  
[2026-06-01] SEGURANÇA: links de presente e URLs de imagem eram passados sem validação para `window.open`/`<img>`/`navigator.clipboard`, permitindo esquemas como `javascript:`/`data:` (vetor de XSS).  
CAUSA: ausência de saneamento de URL externa antes do uso.  
FIX: funções `safeUrl()` (só http/https via construtor `URL`) e `safeImageUrl()` (http/https ou `data:image/`) aplicadas em salvar, importar, render, abrir e copiar link.  
[2026-06-01] Removido o `<select id="priceType">` com única opção "manual" (código morto sem efeito) e o handler dele.

---

## 🔗 INTEGRAÇÕES & SERVIÇOS EXTERNOS

[2026-04-27] Google Fonts — `Space Grotesk` carregada via `<link>` no `<head>`. Sem API key necessária.  
[2026-04-27] GitHub Pages — deploy automático a partir da branch `main` (raiz `/`). URL pública: https://gifts.felixo.com.br  
[2026-04-27] Domínio customizado — CNAME `gifts.felixo.com.br` → `felipe-alcantara.github.io`. Arquivo `CNAME` na raiz do repo.  

---

## 📝 NOTAS GERAIS

[2026-04-27] Estrutura do objeto `gift` no localStorage:
```json
{
  "id": "g_xxxxxxx",
  "title": "string",
  "price": null | number,
  "currency": "R$",
  "url": "string",
  "tags": ["string"],
  "notes": "string",
  "purchased": false,
  "imageData": "string (URL ou base64)",
  "createdAt": 1234567890000,
  "updatedAt": 1234567890000
}
```
[2026-04-27] A propriedade `imageIsURL` foi planejada mas não implementada completamente — `imageData` armazena tanto URLs quanto base64 sem distinção no render.  
[2026-06-01] ✅ Resolvido — `imageIsURL` agora é gravada em `saveGift`/import: `true` quando `imageData` é http(s), `false` quando é `data:image/...`. O render usa `safeImageUrl()` para distinguir e validar a origem.  
[2026-04-27] O arquivo principal foi renomeado de `felixo_gift_organizer_single_file_html.html` para `index.html` para compatibilidade com GitHub Pages.

---

## 🧠 CHAIN OF THOUGHT

[2026-04-27] CONTEXTO: Alinhar cores ao Felixo Design System.  
PENSAMENTO: `--accent: #7c3aed` é roxo padrão, mas o padrão Felixo usa `#A855F7` (Bright) e `#C084FC` (estático).  
PENSAMENTO: Introduzida variável `--accent-soft: #C084FC` para gradientes; `--accent` passou a ser `#A855F7`.  
PENSAMENTO: Sombras do FAB foram atualizadas para o RGB correspondente (168,85,247).  
RESULTADO: Identidade visual alinhada ao Felixo Design System sem quebrar nenhuma funcionalidade.

---

> **Assinatura de Origem**  
> Projeto de **Felipe Martin** — [@Felipe-Alcantara](https://github.com/Felipe-Alcantara)  
> Repositório: https://github.com/Felipe-Alcantara/Organizador-de-presentes-do-Felixo  
> Template IA.md baseado no Felixo System Design.
