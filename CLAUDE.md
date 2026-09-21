```
Template version: 1.1
```

# E-commerce EDA — Análise Exploratória e Testes de Hipóteses (Olist)

## 1. Identidade

- **ID:** ecommerce-eda
- **Nome legível:** E-commerce EDA — Olist Brasil
- **Guia de referência:** `README.md` e `insights.md` neste diretório (projeto herdado com EDA já concluída)
- **Status:** partial:falta-testes-de-hipoteses
- **Repositório GitHub:** a criar / consolidar

## 2. Pré-requisitos

Pré-requisitos: nenhum

## 3. Arquitetura

Projeto de análise exploratória sobre o dataset público **Olist** (e-commerce
brasileiro), entregue em duas fases:

- **Fase concluída (EDA):** carregamento dos CSVs Olist, tratamento de
  valores faltantes, análises descritivas de pedidos, clientes, produtos e
  avaliações, visualizações univariadas e bivariadas. Resultado consolidado
  em `insights.md` e no notebook `Análise_de_Vendas_para_E-commerce_com_Python.ipynb`.
- **Fase pendente (testes de hipóteses):** transformar observações da EDA em
  **hipóteses formais** testadas com inferência estatística — t-test /
  Mann-Whitney para comparação de duas amostras, ANOVA para múltiplos
  grupos, reportando p-valor **junto com tamanho de efeito** (Cohen's d,
  eta-squared).

Data flow: `CSVs Olist → Pandas (limpeza) → EDA (concluída) → hipóteses
formais → testes estatísticos (t-test, Mann-Whitney, ANOVA) → visualizações
finais → relatório`.

## 4. Stack fixada

- Python 3.11+
- `pandas` 2.2.x
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy` (testes estatísticos: `scipy.stats`)
- `jupyter` / `jupyterlab`
- `ruff` (linter/formatter Python)
- `pytest` (testes, quando houver código reutilizável em `src/`)

## 5. Progresso

- [x] Fase 1 — Ingestão: CSVs Olist carregados em `data/`, schemas documentados
- [x] Fase 2 — Limpeza: valores faltantes tratados, tipos corrigidos, joins entre tabelas validados
- [x] Fase 3 — EDA descritiva: distribuições, séries temporais de pedidos, top categorias, geografia de clientes
- [x] Fase 4 — Visualizações exploratórias: gráficos univariados e bivariados em `notebooks/` e `insights.md`
- [ ] Fase 5 — Formulação de hipóteses: lista de ≥5 hipóteses derivadas da EDA registradas em `docs/hipoteses.md`, cada uma com H0 e H1 explícitas ANTES de qualquer teste
- [ ] Fase 6 — Testes de duas amostras: aplicar t-test (com checagem de normalidade via Shapiro e homocedasticidade via Levene) ou Mann-Whitney quando premissas falham; p-valor + Cohen's d registrados
- [ ] Fase 7 — ANOVA: aplicar ANOVA one-way para comparação de ≥3 grupos (ex: categorias de produto × rating médio), com checagem de premissas e eta-squared reportado; Kruskal-Wallis como fallback não-paramétrico
- [ ] Fase 8 — Consolidação: `reports/hypothesis-tests.md` com cada hipótese, teste aplicado, p-valor, tamanho de efeito, conclusão prática e gráfico de suporte; README atualizado referenciando a seção nova

## 6. Patterns

- **Hipótese declarada ANTES do teste:** toda hipótese é registrada em
  `docs/hipoteses.md` com H0 e H1 explícitas antes de qualquer cálculo de
  p-valor. Ordem inversa (testar primeiro, formular depois) é p-hacking.
- **P-valor interpretado junto com tamanho de efeito:** todo teste reporta
  ambos. P-valor sem tamanho de efeito não é conclusão — amostras grandes
  produzem significância estatística trivial.
- **Checagem de premissas explícita:** antes de t-test ou ANOVA, rodar e
  reportar Shapiro-Wilk (normalidade) e Levene (homocedasticidade). Se
  falham, usar Mann-Whitney ou Kruskal-Wallis e documentar a troca.
- **Correção para comparações múltiplas:** quando mais de uma hipótese é
  testada no mesmo conjunto, aplicar Bonferroni ou Benjamini-Hochberg e
  reportar tanto p-valor original quanto ajustado.

## 7. Anti-patterns

- **Nunca fazer p-hacking:** não testar múltiplas variações até encontrar
  p < 0.05. Toda hipótese precisa estar em `docs/hipoteses.md` antes do teste.
- **Nunca interpretar significância sem tamanho de efeito:** "p < 0.05"
  isoladamente não é conclusão prática; precisa vir acompanhado de Cohen's d,
  eta-squared ou diferença absoluta com intervalo de confiança.
- **Nunca confundir correlação com causalidade** nas conclusões, mesmo quando
  o teste é significativo — esta é EDA/inferência, não estudo causal.
- **Nunca rodar t-test em distribuição claramente não-normal com amostra
  pequena:** a checagem Shapiro/Levene é gate, não decoração.

## 8. Segurança

- **Credenciais:** não aplicável — dataset Olist é público, lido de arquivos locais.
- **`.env` no `.gitignore`** por padrão, mesmo sem uso atual, para proteger
  evoluções futuras (ex: carregar dataset de S3).
- **Nunca commitar:** CSVs brutos do Olist em `data/` (volume grande;
  versionar apenas o script de download ou instruções no README),
  outputs pesados de notebooks (limpar outputs antes do commit ou usar
  `nbstripout`).
- **PII:** o dataset Olist é anonimizado na origem, mas revisar qualquer
  agregação por cliente antes de publicar para garantir que não reidentifica.

## 9. Deploy

Reprodução local completa do zero:

1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Baixar dataset Olist do Kaggle para `data/` (instruções no README)
4. `jupyter lab notebooks/` para reexecutar análises exploratórias
5. (fase pendente) `jupyter lab notebooks/hypothesis_tests.ipynb` para os testes estatísticos
6. `pytest` para validar utilitários em `src/` (quando houver)

## 10. Entregáveis

- `insights.md` — consolidação narrativa da EDA (versionado, **existente**)
- `notebooks/Análise_de_Vendas_para_E-commerce_com_Python.ipynb` — notebook principal da EDA (versionado, **existente**)
- `docs/hipoteses.md` — hipóteses formais com H0/H1 (versionado, **a criar na Fase 5**)
- `reports/hypothesis-tests.md` — resultados dos testes com p-valor, tamanho de efeito e conclusão (versionado, **a criar na Fase 8**)
- `notebooks/hypothesis_tests.ipynb` — notebook dos testes estatísticos (versionado sem outputs pesados, **a criar**)
- `portfolio.html` — versão estática para publicação (versionado, **existente**)
- `data/` — CSVs Olist (ignorado, baixado do Kaggle)
- Exposição pública: `portfolio.html` renderizado em GitHub Pages + README com highlights

## 11. Documentação

- **Comentários em Python:** docstrings em funções reutilizáveis em `src/`;
  nos notebooks, a narrativa em markdown substitui comentários — explique
  em células de texto o porquê de cada passo, não só o quê.
- **Notebooks:** cada seção começa com a pergunta que está sendo respondida
  e termina com a conclusão em uma linha.
- **README do projeto:** contexto do dataset Olist, link do Kaggle, como
  rodar, resumo dos insights da EDA, resumo dos testes de hipóteses (após
  Fase 8), link para `portfolio.html`.
- **Relatório de testes (`reports/hypothesis-tests.md`):** uma seção por
  hipótese, sempre no formato: pergunta → H0/H1 → teste escolhido (e por
  quê) → p-valor → tamanho de efeito → conclusão prática → gráfico.

## 12. Log de decisões

<!--
Vazio na criação é esperado. Preencher durante execução, nunca
retroativamente — ADRs inventados a posteriori perdem valor.

Formato por entrada:

### YYYY-MM-DD — <título curto da decisão>
**Decisão:** <o que foi decidido>
**Motivo:** <por que — restrição, trade-off, requisito>
**Alternativas descartadas:** <o que foi considerado e por que não>
-->
