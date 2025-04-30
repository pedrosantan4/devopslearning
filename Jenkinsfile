pipeline {
    agent any
    
    environment {
        MINIO_ENDPOINT = 'http://minio:9000'
        MINIO_ACCESS_KEY = 'minioadmin'
        MINIO_SECRET_KEY = 'minioadmin'
        FLASK_ENDPOINT = 'http://flask:5000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Start Services') {
            steps {
                sh '''
                    docker compose up -d
                    sleep 15  # Aguarda os serviços iniciarem
                '''
            }
        }
        
        stage('Check Services Health') {
            steps {
                sh '''
                    # Verifica se o MinIO está respondendo
                    curl -f http://localhost:9000/minio/health/live || exit 1
                    # Verifica se o Flask está respondendo
                    curl -f http://localhost:5000/health || exit 1
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python3 boto_test.py'
            }
        }
        
        stage('Deploy to Kubernetes') {
            when {
                branch 'main'
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
            sh 'docker compose down'
            cleanWs()
        }
    }
} 