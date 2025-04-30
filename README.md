# Projeto DevOps com Flask, MinIO e Kubernetes

Este projeto demonstra uma aplicação moderna de armazenamento de arquivos usando Flask, MinIO (compatível com S3) e Kubernetes, com pipelines de CI/CD implementados no GitHub Actions e Jenkins.

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com os seguintes objetivos:

1. **Prática com S3/MinIO**:
   - Aprender a criar e gerenciar buckets
   - Implementar upload e download de arquivos
   - Entender a API compatível com S3
   - Gerenciar permissões e acesso

2. **Desenvolvimento com Flask**:
   - Criar APIs RESTful
   - Implementar endpoints para manipulação de arquivos
   - Praticar boas práticas de desenvolvimento Python
   - Integrar com serviços externos (MinIO)

3. **DevOps e Infraestrutura**:
   - Containerização com Docker
   - Orquestração com Kubernetes
   - Implementação de CI/CD
   - Automação de processos

4. **Aprendizado Prático**:
   - Hands-on com tecnologias modernas
   - Experiência com pipelines de CI/CD
   - Prática com orquestração de containers
   - Desenvolvimento de APIs em produção

## 🚀 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Armazenamento**: MinIO (S3-compatible)
- **Containerização**: Docker & Docker Compose
- **Orquestração**: Kubernetes
- **CI/CD**: GitHub Actions & Jenkins
- **Infraestrutura**: AWS EKS (Elastic Kubernetes Service)

## 📋 Pré-requisitos

- Python 3.9+
- Docker e Docker Compose
- kubectl (para deploy no Kubernetes)
- AWS CLI (para deploy no EKS)

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/pedrosantan4/devopslearning.git
cd devopslearning
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

3. Inicie os serviços com Docker Compose:
```bash
docker compose up -d
```

## 🏗️ Estrutura do Projeto

```
.
├── app/
│   └── app.py              # Aplicação Flask
├── k8s/
│   ├── flask-deployment.yaml   # Manifesto Kubernetes para Flask
│   └── minio-deployment.yaml   # Manifesto Kubernetes para MinIO
├── .github/
│   └── workflows/
│       └── main.yml        # Pipeline do GitHub Actions
├── Jenkinsfile            # Pipeline do Jenkins
├── docker-compose.yml     # Configuração do Docker Compose
├── Dockerfile            # Build da imagem Flask
└── requirements.txt      # Dependências Python
```

## 🔄 Fluxo de Funcionamento

1. **Aplicação Flask**:
   - API REST para upload de arquivos
   - Endpoint `/health` para verificação de saúde
   - Integração com MinIO para armazenamento

2. **MinIO**:
   - Serviço compatível com S3
   - Armazenamento persistente via volumes
   - Console web na porta 9001

3. **Docker Compose**:
   - Orquestra Flask e MinIO localmente
   - Configura rede entre containers
   - Gerencia volumes persistentes

4. **Kubernetes**:
   - Deploy em produção via EKS
   - Escalabilidade horizontal
   - Gerenciamento de configuração

## 🚀 CI/CD Pipeline

### GitHub Actions
- Executa em push e pull requests
- Testa a aplicação
- Verifica saúde dos serviços
- Prepara para deploy

### Jenkins
- Pipeline declarativo
- Testes automatizados
- Deploy para Kubernetes
- Limpeza de workspace

## 🔍 Endpoints da API

- `GET /`: Verifica se a API está online
- `GET /health`: Verifica saúde da aplicação
- `POST /upload`: Upload de arquivos para o MinIO

## 🛡️ Segurança

- Credenciais via variáveis de ambiente
- Secrets no Kubernetes
- Autenticação MinIO
- HTTPS em produção

## 📈 Monitoramento

- Health checks implementados
- Logs centralizados
- Métricas de performance
- Alertas configuráveis

## 🚀 Deploy

### Local
```bash
docker compose up -d
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

## 🔧 Configuração

### Variáveis de Ambiente
```env
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
```

### Kubernetes
- Namespace: `default`
- Replicas: 3 (Flask)
- Storage: 10Gi (MinIO)

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **Pedro Santana** - *Desenvolvimento* - [pedrosantan4](https://github.com/pedrosantan4)
- **Adryann Geovanny** - *Desenvolvimento* - [adryanngcosta](https://github.com/adryanngcosta)

## 🙏 Agradecimentos

- Equipe de DevOps
- Comunidade Open Source
- Documentação das tecnologias utilizadas 