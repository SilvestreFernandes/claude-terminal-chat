# 🗺️ Roadmap de Melhorias — Claude Terminal Chat

Objetivo: transformar o script atual (~120 linhas, uma chamada de API) num projeto de
portfólio que demonstre **profundidade em IA aplicada** para vagas de estágio.

Narrativa alvo: **"Assistente de terminal com RAG + ferramentas"**.

Legenda de esforço: 🟢 pequeno (<2h) · 🟡 médio (meio dia) · 🔴 grande (1–3 dias)

---

## Fase 0 — Correções e higiene

- [ ] 🟢 **Bug**: `except AuthenticationError` cita "arquivo .env" que não existe. Ou implementar `.env`, ou corrigir a mensagem.
- [ ] 🟢 Remover fallback `os.environ.get("ANTHROPIC_API_KEY", "sua-api-key-aqui")` — deve falhar explicitamente se a chave não estiver setada.
- [ ] 🟢 Adicionar `python-dotenv` e carregar `.env` de verdade. Criar `.env.example`.
- [ ] 🟢 Type hints completos + docstrings em todas as funções.
- [ ] 🟢 Conferir o `model=` — hoje está `claude-opus-4-5`. Fixar um modelo válido e recente, e torná-lo configurável.

---

## Fase 1 — Base do produto (fazer primeiro)

- [ ] 🟡 **Streaming de respostas** com `client.messages.stream()` — imprimir token a token.
- [ ] 🟡 **Renderização Rich** (`rich`): markdown, syntax highlight em blocos de código, spinner "pensando...".
- [ ] 🟡 **Persistência de sessões**: salvar conversas em SQLite ou JSON em `~/.claude-chat/`.
  - [ ] `--resume` para continuar a última conversa
  - [ ] listar / nomear / apagar conversas
- [ ] 🟢 **Contagem de tokens e custo**: usar `client.messages.count_tokens`, exibir input/output/total e US$ estimado ao sair.
- [ ] 🟢 **Flags de CLI** com `typer` ou `argparse`: `--model`, `--system`, `--resume`, `--no-stream`.
- [ ] 🟢 **Retry com backoff exponencial** em `RateLimitError` / `APIError`.
- [ ] 🟢 **Prompt caching**: marcar o system prompt com `cache_control` (`{"type": "ephemeral"}`).

---

## Fase 2 — Profundidade de IA (o que impressiona)

### RAG — "converse com seus documentos"
- [ ] 🔴 Ingestão de arquivos (`PDF`, `TXT`, `MD`) via flag `--docs ./pasta`.
- [ ] 🟡 Chunking com overlap (ex.: 800 tokens / 100 de overlap).
- [ ] 🟡 Embeddings — escolher um:
  - `voyage-3` (API da Voyage, recomendada pela Anthropic), ou
  - `sentence-transformers` local (offline, sem custo).
- [ ] 🟡 Índice vetorial: `ChromaDB` ou `FAISS`.
- [ ] 🟡 Pipeline de retrieval: top-k por similaridade → injetar trechos no prompt com citação da fonte.
- [ ] 🟢 Mostrar as fontes usadas em cada resposta.

### Tool use / agente
- [ ] 🔴 Definir 2–3 ferramentas reais e o loop de `tool_use` / `tool_result`:
  - [ ] calculadora / avaliação de expressão
  - [ ] ler arquivo do disco
  - [ ] busca web (ou busca nos documentos do RAG)
  - [ ] (opcional) executar snippet de Python em sandbox
- [ ] 🟢 Exibir de forma legível quando o Claude chama uma ferramenta.

### Gestão de janela de contexto
- [ ] 🟡 Monitorar tokens acumulados do histórico.
- [ ] 🟡 Ao passar de um limite, **resumir automaticamente** as mensagens antigas (chamada separada) e substituir pelo resumo.
- [ ] 🟢 Estratégia alternativa: truncamento por janela deslizante, configurável.

---

## Fase 3 — Rigor de ML

- [ ] 🔴 **Mini harness de avaliação** em `evals/`:
  - [ ] ~15–20 casos (pergunta + resposta/critério esperado)
  - [ ] avaliação por asserts simples **e** LLM-as-judge
  - [ ] relatório com métricas (acurácia, custo médio, latência média)
- [ ] 🟡 Rodar os evals no CI (pode ser em job separado / manual por causa de custo de API).
- [ ] 🟢 Documentar resultados no README (tabela de baseline).

---

## Fase 4 — Engenharia e empacotamento

- [ ] 🟡 Refatorar em módulos: `cli.py`, `client.py`, `history.py`, `rag.py`, `tools.py`, `config.py`.
- [ ] 🟢 `config.py` com `pydantic-settings` (config tipada, validada).
- [ ] 🟢 `pyproject.toml` + entry point (`claude-chat`), instalável via `pipx`.
- [ ] 🟡 **Testes** com `pytest` + mock do client Anthropic. Meta: cobrir history, config, RAG, parsing de comandos.
- [ ] 🟢 **GitHub Actions**: `pytest` + `ruff` + `mypy` em cada push/PR.
- [ ] 🟢 `ruff` + `mypy` configurados e passando localmente.
- [ ] 🟢 Logging estruturado (`logging`), nível via `--verbose`.
- [ ] 🟢 **Dockerfile** + instrução de `docker run`.
- [ ] 🟢 **Abstração de provedor**: interface comum + segundo backend (OpenAI ou Ollama local) para mostrar independência de vendor.
- [ ] 🟢 **Personas**: system prompts prontos selecionáveis por flag / arquivo.

---

## Fase 5 — Apresentação (não subestimar)

- [ ] 🟢 **GIF de demo** no topo do README (usar `asciinema` ou `vhs`).
- [ ] 🟢 **Diagrama de arquitetura** (Mermaid) mostrando fluxo: input → RAG → LLM → tools → output.
- [ ] 🟢 Seção "Decisões técnicas" no README explicando *por que* cada escolha (chunk size, top-k, modelo de embedding, estratégia de contexto).
- [ ] 🟢 Seção "Resultados dos evals" com a tabela de baseline.
- [ ] 🟢 Badges reais (CI passando, cobertura de testes).
- [ ] 🟢 Traduzir README para inglês (ou versão bilíngue) — amplia alcance com recrutadores.

---

## Ordem sugerida de execução

1. Fase 0 inteira (rápido, tira arestas).
2. Fase 1: streaming + Rich + persistência + custo.
3. Fase 2: **RAG** primeiro, depois **tool use**, depois contexto.
4. Fase 3: evals (mesmo que pequeno — o diferencial é *ter*).
5. Fase 4: modularizar, testar, CI, empacotar.
6. Fase 5: README, GIF, diagrama — feito em paralelo, conforme cada feature fica pronta.

> Dica para entrevista: cada item da Fase 2 e 3 sustenta ~5 min de conversa técnica
> (embeddings, agentes, avaliação, controle de custo). É isso que separa
> "fiz um chatbot" de "sei construir um sistema de IA".
