<div align="center">
  <img src="reports/figures/banner.svg" width="100%" alt="Banner Análise de Vendas">
</div>

# 🎯 Maximizando Receita E-commerce: Insights Estratégicos de Vendas

> Uma análise exploratória profunda para identificar padrões de consumo, sazonalidade e oportunidades de expansão logística.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Status: Concluído](https://img.shields.io/badge/Status-Concluído-success?style=flat-square)

## 📌 Problema de Negócio

Uma loja de e-commerce em crescimento enfrentava baixa visibilidade sobre sua performance real. Sem dados claros, a gestão de estoque era ineficiente, as campanhas de marketing eram genéricas e o planejamento de expansão carecia de fundamentos geográficos. 

O objetivo deste projeto foi transformar 500 registros de transações em **diretrizes estratégicas acionáveis** respondendo: o que vender, quando agir, onde focar e para onde expandir.

## 🔍 Abordagem

1.  **Tratamento de Dados:** Conversão de tipos, limpeza e engenharia de atributos (Cálculo de Faturamento).
2.  **Análise Temporal:** Identificação de tendências e sazonalidades mensais.
3.  **Análise de Mix:** Decomposição da receita por categoria e volume por produto.
4.  **Geolocalização:** Mapeamento do consumo regional vs. eficiência de entrega.

## 📊 Resultados e Descobertas

> 💡 **Hero Metric:** Ticket Médio por Venda de **R$ 3.850,00**, impulsionado pela alta tração da categoria de Eletrônicos.

### Tabela de Insights de Negócio

| Perspectiva | Descoberta Principal | Recomendação Estratégica |
| :--- | :--- | :--- |
| **Produtos** | Monitor Ultrawide e Teclado Mecânico lideram em volume. | Priorizar estoque e bundles de periféricos high-end. |
| **Sazonalidade** | Crescimento sustentado no Q1 com pico absoluto em Março. | Antecipar estoques e campanhas no final de Fevereiro. |
| **Geografia** | O eixo SP-RJ-MG concentra a maior densidade de receita. | Focar investimentos de mídia e logística expressa no Sudeste. |
| **Categorias** | Eletrônicos dominam 60%+ do faturamento total. | Expandir catálogo de Laptops e GPUs (alto ticket). |

## 📈 Visualizações Principais

<div align="center">
  <img src="reports/figures/top_10_produtos.png" width="80%" alt="Top 10 Produtos">
  <br>
  <em>Figura 1: Volume de vendas por item — periféricos de performance dominam a demanda.</em>
</div>

<br>

<div align="center">
  <img src="reports/figures/faturamento_mensal.png" width="80%" alt="Faturamento Mensal">
  <br>
  <em>Figura 2: Evolução temporal — tendência de alta no primeiro trimestre de 2024.</em>
</div>

<br>

<div align="center">
  <img src="reports/figures/faturamento_por_categoria.png" width="80%" alt="Faturamento por Categoria">
  <br>
  <em>Figura 3: Composição da receita — Eletrônicos como motor principal do negócio.</em>
</div>

<br>

<div align="center">
  <img src="reports/figures/faturamento_por_estado.png" width="80%" alt="Distribuição Geográfica">
  <br>
  <em>Figura 4: Mapa de calor de faturamento — validação da logística rápida no eixo Sudeste.</em>
</div>

## 🛠️ Stack Tecnológica

*   **Linguagem:** Python 3.13
*   **Bibliotecas:** Pandas (Manipulação), NumPy (Processamento), Matplotlib & Seaborn (Visualização)
*   **Documentação:** Jupyter Notebook, Shields.io

## 📁 Estrutura do Projeto

```text
├── data/               # Datasets gerados e processados
├── notebooks/          # Analise_Vendas_Ecommerce.ipynb
├── reports/            # Figuras exportadas com save_fig()
├── src/                # Scripts auxiliares
└── requirements.txt    # Dependências do ambiente
```

## 🚀 Como Reproduzir

1.  Garanta que tem o **Python 3.10+** instalado.
2.  Clone o repositório.
3.  Instale as dependências: `pip install -r requirements.txt`.
4.  Execute o notebook: `jupyter notebook notebooks/Analise_Vendas_Ecommerce.ipynb`.
5.  O projeto utiliza dados sintéticos gerados dinamicamente via script.

---
**Desenvolvido por Athos** - [GitHub](https://github.com/athosroque)
