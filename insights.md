# 📊 Relatório de Insights: Análise de Vendas E-commerce

Este documento apresenta uma síntese estratégica dos principais achados extraídos da análise exploratória de dados de vendas. Para a metodologia técnica completa, consulte o [Notebook de Análise](notebooks/Analise_Vendas_Ecommerce.ipynb).

---

## 1. Principais Insights de Negócio

### 📦 O que vender — Mix de Produtos
O ranking de produtos revelou uma concentração clara de demanda em periféricos e componentes de alta performance:
- **Produtos Top 3:** **Mouse Sem Fio**, **SSD 1TB** e **Teclado Mecânico**. 
- **Impacto:** Estes três itens representam juntos aproximadamente **34%** do total de pedidos.
- **Observação:** O **Mouse Sem Fio** liderou de forma absoluta com **60** unidades vendidas.
- **Oportunidade:** Produtos como **Gabinete ATX** registraram o menor volume, sinalizando potencial para revisão de precificação ou criação de pacotes promocionais.

> 💡 **Ação Recomendada:** Garantir estoque prioritário para o Top 3. Analisar a inclusão do "Gabinete" em bundles com "Placas de Vídeo" para acelerar o giro de estoque.

### 📅 Quando agir — Sazonalidade Mensal
A evolução temporal expôs variações significativas no faturamento ao longo do primeiro trimestre:
- **Mês de Pico:** **Fevereiro**, atingindo **R$ 1,63 Milhão** em receita bruta.
- **Aderência:** O faturamento médio mensal estabilizou-se em **R$ 1,5 Mi**.
- **Variação:** Identificamos uma variação de até **65%** entre o mês de pico e períodos de baixa (ajustados pela janela de coleta de dados).

> 💡 **Ação Recomendada:** Planejar campanhas de marketing agressivas em Janeiro para "antecipar" a demanda de Fevereiro. Escalar a verba de tráfego pago 15 dias antes das janelas de alto volume.

### 🏷️ Onde focar — Categorias de Receita
A hierarquia de faturamento é dominada por itens de alto ticket médio:
- **Líder Absoluto:** **Eletrônicos**, concentrando sozinho **R$ 3,02 Milhões** (**58%** da receita total).
- **Segmentos Secundários:** **Hardware** (**R$ 1,42 Mi**) e **Acessórios** ocupam posições intermediárias.
- **Base da Cauda:** **Móveis** responde pela menor parcela (**R$ 336k**).

> 💡 **Ação Recomendada:** Expandir o catálogo de Eletrônicos (Laptops e GPUs), que combinam alta demanda com faturamento expressivo. Para Acessórios, implementar estratégias de *upsell* no carrinho de compras.

### 🗺️ Para onde expandir — Geografia e Logística
A densidade de vendas valida a estratégia de presença forte no Sudeste:
- **Estado Líder:** **Minas Gerais (MG)** com **R$ 905k** em faturamento.
- **Potencial Nordeste:** **Bahia (BA)** surge como o segundo maior mercado (**R$ 820k**), indicando forte tração orgânica.
- **Eixo Estratégico:** O eixo **MG-RJ-SP** representa **41%** das transações totais da loja.

> 💡 **Ação Recomendada:** Centralizar investimentos logísticos e centros de distribuição avançados no eixo Sudeste para garantir entregas em < 24h. Avaliar parcerias de frete para o Nordeste para reduzir o custo de entrega em regiões de alto volume como BA e CE.

---

## 2. Resumo Executivo para Tomada de Decisão

| Perspectiva | Achado Principal | Recomendação Estratégica |
|-------------|-----------------|------------------|
| **Produtos** | Top 3 concentram **~34%** dos pedidos | Otimizar Curva A de estoque |
| **Sazonalidade** | Pico em **Fevereiro** (**R$ 1,63 Mi**) | Antecipar verba de Marketing |
| **Categorias** | **Eletrônicos** = **58%** da receita | Diversificar SKUs de alto ticket |
| **Geografia** | **Eixo MG-RJ-SP** = **41%** das vendas | Logística expressa prioritária |

---

## 3. Próximos Passos Sugeridos
1. **Análise de Cohort:** Mapear o ciclo de vida e recorrência dos clientes.
2. **Previsão de Demanda:** Implementar modelos de Machine Learning para forecasting de estoque.
3. **Dashboards:** Migrar estes insights para um ambiente de BI interativo (Power BI/Tableau).

---
**Documento gerado como parte do projeto de Portfólio de Data Science.**
[Voltar para o Repositório Principal](../README.md)
