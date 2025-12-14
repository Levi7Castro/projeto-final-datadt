# 🚀 Projeto Final: Da Operação ao Preditivo – Vendas e Finanças


## 🎯 1. Visão Geral e Contexto de Negócio

Este projeto de Engenharia de Dados e Machine Learning visa modernizar a tomada de decisão de uma empresa de varejo, que busca evoluir de relatórios puramente operacionais para uma gestão baseada em dados (Data-Driven).

A solução transforma dados transacionais brutos de **Vendas**, **Contas a Receber** e **Contas a Pagar** em insights preditivos e acionáveis, com foco na otimização das áreas de marketing e cobrança.

### 🔑 Objetivos Principais

* **Pipeline ETL:** Construção de um pipeline robusto em Python (Extração → Transformação → Qualidade → Carga).
* **Data Warehouse (DW):** Modelagem de um DW em esquema estrela (*Star Schema*) no SQL Server, integrando domínios de Vendas e Financeiro.
* **Data Lake:** Disponibilização de um *slice* analítico particionado em formato Parquet no Hadoop (HDFS).
* **Machine Learning (ML):** Treinamento e avaliação de modelos preditivos para resolver problemas de negócio, tais como:
    * *Classificação:* Probabilidade de Recompra em 90 dias.
    * *Classificação:* Risco de Atraso no Pagamento.

---

## 🧱 2. Arquitetura da Solução

O projeto implementa um fluxo de dados *End-to-End*, desde a origem transacional até o consumo analítico e preditivo.

### 2.1 Tecnologias Utilizadas

| Camada | Ferramenta | Descrição |
| :--- | :--- | :--- |
| **Origem** | PostgreSQL | Base de dados transacional (OLTP). |
| **Orquestração** | Apache Airflow | Agendamento e automação de DAGs reprodutíveis. |
| **ETL & Processamento** | Python | Uso de Pandas, SQLAlchemy e PyArrow para manipulação de dados. |
| **Data Warehouse** | SQL Server | Banco de dados analítico (OLAP). |
| **Data Lake** | Hadoop/HDFS | Armazenamento de *slices* em Parquet particionado. |
| **Machine Learning** | Scikit-learn, XGBoost | Treinamento, avaliação e scoring de modelos. |
| **Versionamento** | Git | Controle de versão do código-fonte. |

### 2.2 Estrutura do Repositório

```bash
projeto-final-datadt/
├── airflow/            # DAGs e scripts para orquestração no Apache Airflow
│   ├── dags/
│   └── requirements.txt
├── etl/                # Scripts Python (Extração, Transformação e Carga)
├── dw/                 # Scripts SQL (DDL e DML) para o SQL Server
├── lake/               # Scripts para geração do Slice Parquet no HDFS
├── ml/                 # Notebooks de modelagem e scripts de scoring
├── docs/               # Diagramas de arquitetura e documentação de projeto
├── .env                # Variáveis de ambiente (NÃO VERSIONADO)


-----

## 🛠️ 3. Configuração e Execução

### 3.1 Credenciais da Fonte de Dados (Segurança)

⚠️ **ATENÇÃO:** As credenciais de acesso ao banco transacional **não devem** ser "commitadas" diretamente no código. Utilize um arquivo `.env` na raiz do projeto para armazená-las com segurança.

Exemplo de estrutura do arquivo `.env`:

```ini
DB_HOST=postgresql-datadt.alwaysdata.net
DB_NAME=datadt_digital_corporativo
DB_USER=seu_usuario_aqui
DB_PASS=sua_senha_aqui
```

### 3.2 Setup do Ambiente Local

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


    ```

3.  **Instale as Dependências:**

    ```bash
    pip install -r airflow/requirements.txt
    ```

### 3.3 Ordem de Execução do Pipeline

Para garantir a reprodutibilidade do projeto ("do zero ao fim"), execute os passos na seguinte ordem (manualmente ou via Airflow):

1.  **Criação do DW:** Executar scripts DDL localizados em `dw/` para criar as tabelas no SQL Server.
2.  **Carga ETL:** Rodar o script principal em `etl/` para realizar a carga (Staging → DW).
3.  **Exportação para o Lake:** Rodar o script em `lake/` para gerar os arquivos Parquet no HDFS.
4.  **Modelagem ML:** Executar os notebooks em `ml/` para treinar e avaliar o modelo preditivo.

-----

## 📈 4. Critérios de Avaliação e Entregáveis

| Entregável | Detalhes | Métricas de Qualidade |
| :--- | :--- | :--- |
| **Modelagem DW** | Modelo de Dados e scripts SQL (DDL/DML) na pasta `dw/`. | Integridade referencial e normalização dimensional. |
| **Carga ETL** | Scripts Python funcionais em `etl/`. | Reprodutibilidade e tratamento de erros. |
| **Data Lake** | Arquivos Parquet em `hdfs/` ou simulado localmente. | Particionamento eficiente (ex: ano/mês). |
| **Modelo Preditivo** | Notebooks de modelagem na pasta `ml/`. | **Classificação:** AUC, Recall@10%. <br> **Regressão:** MAE, sMAPE. |
| **Exportação ML** | Modelo treinado (`.joblib`) e pipeline de scoring. | Capacidade de predição em novos dados. |
| **Documentação** | Diagrama de arquitetura em `docs/`. | Clareza nas "assunções" de negócio. |
| **Relatório Final** | Análise de KPIs e Plano de Ação. | Relevância dos insights para o negócio. |

