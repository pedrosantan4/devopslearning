pipeline {
    agent any
    
    environment {
        MINIO_ENDPOINT = 'http://minio:9000'
        MINIO_ACCESS_KEY = 'minioadmin'
        MINIO_SECRET_KEY = 'minioadmin'
        FLASK_ENDPOINT = 'http://flask:5000'
        AIRFLOW_HOME = '/opt/airflow'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Check README Changes') {
            steps {
                script {
                    def changedFiles = sh(
                        script: 'git diff --name-only HEAD^ HEAD',
                        returnStdout: true
                    ).trim().split('\n')
                    
                    def isReadmeOnly = changedFiles.size() == 1 && changedFiles[0] == 'README.md'
                    env.SKIP_TESTS = isReadmeOnly.toString()
                }
            }
        }
        
        stage('Setup Python') {
            when {
                expression { return env.SKIP_TESTS != 'true' }
            }
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Start Services') {
            when {
                expression { return env.SKIP_TESTS != 'true' }
            }
            steps {
                sh '''
                    docker compose up -d
                    sleep 30  # Aguarda os serviços iniciarem
                '''
            }
        }
        
        stage('Check Services Health') {
            when {
                expression { return env.SKIP_TESTS != 'true' }
            }
            steps {
                sh '''
                    # Verifica se o MinIO está respondendo
                    curl -f http://localhost:9000/minio/health/live || exit 1
                    # Verifica se o Airflow está respondendo
                    curl -f http://localhost:8080/health || exit 1
                '''
            }
        }
        
        stage('Run ETL Test') {
            when {
                expression { return env.SKIP_TESTS != 'true' }
            }
            steps {
                script {
                    // Executa o ETL manualmente
                    sh '''
                        python3 -c "
from etl.extractors.cep_extractor import CEPExtractor
from etl.transformers.cep_transformer import CEPTransformer
from etl.loaders.cep_loader import CEPLoader
from etl.utils.cep_finder import CEPFinder

# Inicializa componentes
cep_finder = CEPFinder()
extractor = CEPExtractor()
transformer = CEPTransformer()
loader = CEPLoader()

# Obtém CEPs de SP
ceps = cep_finder.find_ceps_by_state('SP')
if ceps.empty:
    print('Nenhum CEP encontrado para o estado SP')
    exit(1)

print(f'Processando {len(ceps)} CEPs')

# Lista para armazenar todos os dados
all_data = []

# Processa cada CEP
for _, cep_info in ceps.iterrows():
    try:
        cep = cep_info['cep']
        nome = cep_info['nome']
        
        print(f'Processando CEP: {cep} ({nome})')
        
        # Extrai dados
        raw_data = extractor.extract_cep_data(cep)
        
        if not raw_data:
            print(f'Nenhum dado encontrado para o CEP {cep}')
            continue
        
        # Adiciona informações do local
        raw_data['nome_local'] = nome
        all_data.append(raw_data)
        
    except Exception as e:
        print(f'Erro ao processar CEP {cep}: {str(e)}')
        continue

if not all_data:
    print('Nenhum dado coletado para processar')
    exit(1)

# Transforma os dados
print('Transformando dados...')
df = transformer.transform_batch(all_data)

if df.empty:
    print('Nenhum dado válido após transformação')
    exit(1)

# Carrega os dados
print('Carregando dados...')
if not loader.load_data(df):
    print('Falha ao carregar dados')
    exit(1)

print('ETL concluído com sucesso!')
"
                    '''
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            when {
                branch 'main'
                expression { return env.SKIP_TESTS != 'true' }
            }
            steps {
                sh '''
                    aws eks update-kubeconfig --name meu-cluster
                    kubectl apply -f k8s/
                '''
            }
        }
    }
    
    post {
        always {
            script {
                if (env.SKIP_TESTS != 'true') {
                    sh 'docker compose down'
                }
            }
            cleanWs()
        }
    }
} 