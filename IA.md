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

---

## 🔗 INTEGRAÇÕES & SERVIÇOS EXTERNOS

[2026-04-27] Google Fonts — `Space Grotesk` carregada via `<link>` no `<head>`. Sem API key necessária.  
[2026-04-27] Sem outras integrações externas — aplicação totalmente offline após carregamento da fonte.  

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
