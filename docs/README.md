# 🚀 Projeto Final: Da Operação ao Preditivo – Vendas e Finanças

## 🎯 1. Visão Geral e Contexto de Negócio

[cite_start]Este projeto de Engenharia de Dados e Machine Learning visa modernizar a tomada de decisão de uma empresa de varejo, que busca evoluir de relatórios operacionais para uma gestão baseada em dados[cite: 3].

[cite_start]A solução transforma dados transacionais de **Vendas**, **Contas a Receber** e **Contas a Pagar** [cite: 5, 6, 7] [cite_start]em insights preditivos e acionáveis, focando em otimizar as áreas de marketing e cobrança[cite: 15].

### [cite_start]🔑 Objetivos do Projeto [cite: 17]

* [cite_start]**Pipeline ETL:** Construir um pipeline ETL em Python (extração → transformação → qualidade → carga)[cite: 18].
* [cite_start]**Data Warehouse (DW):** Modelar um DW em esquema estrela no SQL Server, integrando as áreas Vendas e Financeiro[cite: 14, 19].
* [cite_start]**Data Lake:** Publicar um *slice* analítico particionado em formato Parquet no Hadoop (HDFS)[cite: 20].
* [cite_start]**Machine Learning (ML):** Treinar e avaliar modelos preditivos a partir do Data Lake para problemáticas de negócio, como **Recompra em 90 dias** (Classificação) ou **Atraso no Pagamento** (Classificação)[cite: 21, 22, 23].

## 🧱 2. Arquitetura da Solução

O projeto segue um fluxo de dados completo, desde a origem transacional até o consumo analítico e preditivo. 

### [cite_start]2.1 Tecnologias Utilizadas [cite: 27, 28, 29, 30]

| Camada | Ferramenta/Requisito | Detalhe |
| :--- | :--- | :--- |
| **Origem** | PostgreSQL | Base de dados transacional. |
| **Orquestração** | Apache Airflow | [cite_start]Agendamento e automação reprodutível[cite: 16]. |
| **ETL & Data Lake** | Python (Pandas, pyodbc/SQLAlchemy, pyarrow) | Linguagem de processamento e bibliotecas de dados. |
| **Data Warehouse** | SQL Server | [cite_start]Banco de dados analítico (instância local ou remota)[cite: 14, 28]. |
| **Data Lake** | Hadoop/HDFS (Parquet) | [cite_start]Armazenamento de *slice* particionado pronto para ML[cite: 29]. |
| **Machine Learning** | scikit-learn, LightGBM/XGBoost | Treinamento e avaliação de modelos preditivos. |
| **Versionamento** | Git | [cite_start]Controle de código-fonte[cite: 31]. |

### 2.2 Estrutura do Repositório

projeto-final-datadt/ ├── airflow/ # Scripts e DAGs para orquestração (Agendamento no Aiflow ) │ ├── dags/ │ └── requirements.txt ├── etl/ # Scripts Python de Extração, Transformação e Carga (ETL Python ) ├── dw/ # Scripts SQL de DDL e DML para o SQL Server (Data Warehouse ) ├── lake/ # Scripts para gerar o Slice Parquet no HDFS (Data Lake ) ├── ml/ # Notebooks de modelagem (Notebook de modelagem ) e scoring ├── docs/ # Arquitetura & Documentação (Diagrama do fluxo ) ├── reports/ # Painel/Relatório final com KPIs e Plano de ação  ├── .env # Variáveis de ambiente (IGNORADO) └── README.md

## 🛠️ 3. Configuração e Execução

### 3.1 Credenciais da Fonte de Dados

As credenciais para acesso ao PostgreSQL transacional são:

* **Host:** `postgresql-datadt.alwaysdata.net` [cite: 9]
* **Database:** `datadt_digital_corporativo` [cite: 10]
* **User:** `datadt_data_analytics` [cite: 11]
* **Password:** `DataAnalytics$100` [cite: 12]

***REGRAS DE OURO:** Estas credenciais devem ser armazenadas em um arquivo `.env` para evitar exposição e garantir a privacidade[cite: 58].*

### 3.2 Setup do Ambiente

1.  **Clone o Repositório:**
    ```bash
    git clone [link-do-seu-repositorio]
    cd projeto-final-datadt
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Linux/macOS
    source ./.venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r airflow/requirements.txt
    ```

### 3.3 Ordem de Execução do Pipeline (Reprodutível) [cite: 56]

Para garantir a reprodutibilidade ("do zero ao fim"), o pipeline deve ser executado na seguinte ordem (ou orquestrado pelo Airflow):

1.  **Criação do DW:** Executar os scripts DDL em `dw/` no SQL Server.
2.  **Carga ETL:** Rodar o script principal em `etl/` para carga no SQL Server (Staging → DW)[cite: 39].
3.  **Exportação para o Lake:** Rodar o script em `lake/` para gerar o Parquet particionado no HDFS[cite: 40].
4.  **Modelagem ML:** Executar o notebook/script em `ml/` para Treinar e Avaliar o modelo[cite: 44, 45].

## 📈 4. Critérios de Avaliação (Entregáveis Principais)

| Entregável | Detalhes | Métricas/Qualidade |
| :--- | :--- | :--- |
| **Modelagem DW** | Modelo de Dados e scripts SQL (DDL/DML) em `dw/`[cite: 37]. |
| **Carga ETL** | Scripts Python funcionais e reprodutíveis em `etl/`[cite: 38, 56]. |
| **Data Lake** | Slice Parquet em `hdfs/` com particionamento útil (ex.: ano/mês)[cite: 43]. |
| **Modelo Preditivo** | Notebook/Script de modelagem em `ml/`. | Classificação: **AUC**, **PR-AUC**, **Recall@k (k=10%)**[cite: 46]. Regressão: **MAE** e **sMAPE**[cite: 47]. |
| **Exportação ML** | Exportação do modelo treinado (`.joblib`) e pipeline de *scoring*[cite: 48]. |
| **Documentação** | Diagrama de arquitetura em `docs/` e documentação de "assunções"[cite: 34, 55]. |
| **Relatório Final** | KPIs, distribuição de scores e **Plano de ação**[cite: 51, 52]. |