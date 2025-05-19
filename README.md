# 📊 Resultados do Censo Escolar 2024  
**Disciplina:** IMD1151 - Ciências de Dados - T01 (2025.1)

## Tema
Análise dos números de alunos da Educação Básica na **Educação Especial** (inclusiva ou exclusiva) com base nos dados do **Censo Escolar 2024**.

📁 **Fonte oficial:**  
[gov.br - INEP - Censo Escolar 2024](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/resultados)

**Aluno:** Douglas Alexandre dos Santos  
**Matrícula:** 20210096853

---

## 📂 Estrutura do Projeto

### 🔍 `processing_data_2024.ipynb` — Tratamento de Dados
Este notebook trata os dados brutos com base no Dicionário de Dados do INEP:

- Filtragem por **Situação de Funcionamento**  
- Verificação de **Dados Ausentes**  
- Classificação das escolas como **Públicas** ou **Privadas**  
- Exportação das **Tabelas Tratadas** para análise posterior

---

### 📈 `analysis_data_2024.ipynb` — Análise e Geração de Gráficos

Análises realizadas com base nas tabelas tratadas:

#### 📍 Distribuição das Escolas
- Quantidade de escolas (públicas e privadas) por **região**
- Quantidade de escolas (públicas e privadas) por **estado**

#### 📦 Matrículas
- **Boxplot** do número de matrículas por tipo de escola (pública/privada)
- Média de matrículas por **região**
- Média de matrículas por **estado**

#### 🧑‍🏫 Educação Especial
- Total de escolas que oferecem Educação Especial por **região**
- Total de escolas que oferecem Educação Especial por **estado**
- Total de **matrículas** na Educação Especial por **região**
- Total de **matrículas** na Educação Especial por **estado**

#### 🔄 Proporções de Atendimento
- Proporção entre **Educação Especial Inclusiva x Exclusiva** por **estado** (rede pública)
- Proporção entre **Educação Especial Inclusiva x Exclusiva** por **estado** (rede privada)

#### 🏫 Comparativos de Turmas
- Comparação do número de turmas **Básicas** e **Inclusivas** nas escolas **públicas** por região
- Comparação do número de turmas **Básicas**, **Inclusivas** e **Exclusivas** nas escolas **privadas** por região

#### 📊 Indicadores Regionais
- Média de alunos da Educação Especial por **região**

#### 🔗 Indicadores e Correlações
- Mapa de correlação para variáveis da **rede pública**
- Mapa de correlação para variáveis da **rede privada**

---

## ✅ Objetivo

Este projeto tem como objetivo fornecer insights quantitativos e visuais sobre a oferta e distribuição da **Educação Especial** no Brasil, com foco na distinção entre redes públicas e privadas de ensino.