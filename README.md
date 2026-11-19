# Painel Analítico — Programa Bolsa Família (2004–2026)

## 1. Título, Tema e Justificativa
**Tema:** Análise histórica e regional dos repasses federais do Programa Bolsa Família (2004–2026).  
**Justificativa:** O Bolsa Família é uma das principais políticas públicas de transferência de renda e combate à pobreza no Brasil. Analisar sua evolução histórica, distribuição regional e estadual, média de famílias atendidas e valor médio do benefício permite compreender o alcance e a dinâmica orçamentária do programa ao longo do tempo de forma visual e acessível.

## 2. Fonte da API de Dados e Descrição dos Dados
* **Fonte / API utilizada:** [Portal Brasileiro de Dados Abertos (dados.gov.br) — Bolsa Família: Benefícios Básicos e Variáveis](https://dados.gov.br/dados/conjuntos-dados/bolsa-familia---beneficios-basicos-e-variaveis)
* **Armazenamento local:** O arquivo bruto obtido foi salvo em `data/raw/bolsa_familia_api.csv` e processado pelo script `src/processamento.py`, gerando `data/processed/bolsa_familia_processado.csv`.
* **Descrição dos dados:** Os dados possuem ano, mês, região, UF, valor repassado, quantidade de famílias atendidas e valor médio do benefício (série de 2004 a 2026, com marcação de anos interpolados `*` onde aplicável).
* **Notebook de teste no Colab:** [Abrir notebook de testes no Google Colab](https://colab.research.google.com/drive/1DbsuVgueapr2SRJkPTdcolJL9WvVPzQZ?usp=sharing)

## 3. Perguntas-Chave Respondidas pelo Dashboard
1. Como evoluiu o volume total de repasses do Bolsa Família na série histórica de 2004 a 2026?
2. Qual foi a variação anual do repasse em relação ao ano anterior no recorte selecionado?
3. Como os recursos se distribuem entre as regiões e os estados (UFs) do Brasil?
4. Qual o comportamento mensal dos repasses, da média de famílias atendidas e do benefício médio no ano analisado?

## 4. Como Rodar o Projeto Localmente
1. Clone este repositório:
   ```bash
   git clone [https://github.com/lukaslmatos/pbf-2026.git](https://github.com/lukaslmatos/pbf-2026.git)
   cd pbf-2026

## 5. Capturas de Tela e Contexto do Dashboard
<img width="920" height="163" alt="1" src="https://github.com/user-attachments/assets/ca9bf771-1770-4a88-885b-6ec4ad1c38fb" />
Indicadores pricipais

<img width="926" height="374" alt="2" src="https://github.com/user-attachments/assets/9cef45e1-5a48-469f-87f8-f86ae4aa6b19" />
Repasses por região / Repasses por estado

<img width="926" height="383" alt="3" src="https://github.com/user-attachments/assets/36d4b4d3-2f32-4e92-baea-f8f13d682d46" />


