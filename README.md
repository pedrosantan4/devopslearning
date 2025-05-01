# Projeto ETL de CEPs

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para dados de CEPs brasileiros, utilizando Apache Airflow para orquestração e MinIO para armazenamento.

## 🏗️ Arquitetura

O projeto é composto por:

### 1. ETL Pipeline
- **Extração**: Busca dados de CEPs através da API ViaCEP
- **Transformação**: Processa e estrutura os dados
- **Carregamento**: Armazena os dados no MinIO

### 2. Infraestrutura
- **Apache Airflow**: Orquestração do pipeline
- **MinIO**: Armazenamento de objetos (S3-compatible)
- **Docker**: Containerização dos serviços

## 📁 Estrutura do Projeto

```
.
├── dags/                    # DAGs do Airflow
│   └── cep_etl_dag.py      # DAG principal do ETL de CEPs
├── etl/                     # Código do pipeline ETL
│   ├── extractors/         # Módulos de extração
│   │   └── cep_extractor.py
│   ├── transformers/       # Módulos de transformação
│   │   └── cep_transformer.py
│   ├── loaders/           # Módulos de carregamento
│   │   └── cep_loader.py
│   └── utils/             # Utilitários
│       └── cep_finder.py
├── docker-compose.yml      # Configuração dos containers
└── requirements.txt        # Dependências Python
```

## 🚀 Como Executar

### Pré-requisitos
- Docker
- Docker Compose
- Python 3.8+

### 1. Clone o Repositório
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Inicie os Serviços
```bash
docker-compose up -d
```

### 4. Acesse as Interfaces
- Airflow: http://localhost:8080
  - Usuário: airflow
  - Senha: airflow
- MinIO: http://localhost:9001
  - Usuário: minioadmin
  - Senha: minioadmin

## 🔄 Pipeline ETL

### 1. Extração (CEPExtractor)
- Busca dados de CEPs através da API ViaCEP
- Endpoint: https://viacep.com.br/ws/{cep}/json/
- Dados extraídos: CEP, logradouro, complemento, bairro, localidade, UF

### 2. Transformação (CEPTransformer)
- Processa os dados brutos
- Adiciona metadados (timestamp, fonte)
- Valida e limpa os dados
- Estrutura em DataFrame pandas

### 3. Carregamento (CEPLoader)
- Conecta ao MinIO (endpoint: http://minio:9000)
- Cria bucket `cep-data` se não existir
- Salva arquivo CSV no formato: `raw/YYYYMMDD_cep_data.csv`

## 📊 DAG do Airflow

### Configuração
- Nome: `cep_etl`
- Schedule: Diário
- Timeout: 30 segundos
- Retries: 0

### Tasks
1. `run_etl`: Executa o pipeline completo
   - Busca 3 CEPs de SP
   - Extrai dados
   - Transforma
   - Carrega no MinIO

## 🔍 Monitoramento

### Logs
- Airflow: Interface web (http://localhost:8080)
- MinIO: Interface web (http://localhost:9001)

### Verificação de Dados
1. Acesse MinIO (http://localhost:9001)
2. Navegue até o bucket `cep-data`
3. Verifique o arquivo mais recente em `raw/`

## 🛠️ Desenvolvimento

### Estrutura de Código
- **CEPExtractor**: Responsável pela extração de dados
- **CEPTransformer**: Processa e estrutura os dados
- **CEPLoader**: Gerencia o carregamento no MinIO
- **CEPFinder**: Utilitário para buscar CEPs por estado

### Convenções
- Nomes de classes: PascalCase
- Nomes de funções: snake_case
- Documentação: Docstrings em português
- Logs: Nível INFO para operações normais, ERROR para falhas

## 🔒 Segurança

### Credenciais
- MinIO:
  - Access Key: minioadmin
  - Secret Key: minioadmin
- Airflow:
  - Usuário: airflow
  - Senha: airflow

### Boas Práticas
- Credenciais em variáveis de ambiente
- Logs sem informações sensíveis
- Timeouts configurados
- Tratamento de erros

## 🧪 Testes

### Execução Manual
```bash
python etl/run_etl.py
```

### Pipeline CI/CD
- Jenkins: Executa testes e deploy
- Verifica saúde dos serviços
- Testa o pipeline ETL
- Deploy para Kubernetes (se na branch main)

## 📈 Próximos Passos

1. Adicionar mais estados além de SP
2. Implementar validação de dados
3. Adicionar métricas de qualidade
4. Expandir cobertura de testes
5. Implementar monitoramento

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 