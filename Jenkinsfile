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
                    sleep 15  # Aguarda os serviços iniciarem
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
                    # Verifica se o Flask está respondendo
                    curl -f http://localhost:5000/health || exit 1
                '''
            }
        }
        
        stage('Run Tests') {
            when {
                expression { return env.SKIP_TESTS != 'true' }
            }
            steps {
                sh 'python3 boto_test.py'
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