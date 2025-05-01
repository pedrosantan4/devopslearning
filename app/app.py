from flask import Flask, request
import boto3
import os
import logging

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração do cliente S3/MinIO
s3 = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    verify=False
)

# Nome do bucket
BUCKET_NAME = "weather-data"

# Cria o bucket se não existir
try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    logger.info(f"Bucket '{BUCKET_NAME}' já existe.")
except:
    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
        logger.info(f"Bucket '{BUCKET_NAME}' criado com sucesso!")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        logger.info(f"Bucket '{BUCKET_NAME}' já existe e pertence a você.")
    except s3.exceptions.BucketAlreadyExists:
        logger.info(f"Bucket '{BUCKET_NAME}' já existe.")

@app.route("/")
def home():
    return "API online!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        logger.info(f"Arquivo {file.filename} enviado com sucesso para o bucket {BUCKET_NAME}")
        return f"Arquivo {file.filename} enviado com sucesso!"
    except Exception as e:
        logger.error(f"Erro ao fazer upload: {str(e)}")
        return f"Erro ao fazer upload: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
