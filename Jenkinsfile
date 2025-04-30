pipeline {
    agent any
    
    environment {
        MINIO_ENDPOINT = 'http://minio:9000'
        MINIO_ACCESS_KEY = 'minioadmin'
        MINIO_SECRET_KEY = 'minioadmin'
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
            cleanWs()
        }
    }
} 