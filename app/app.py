from flask import Flask, request
import boto3
import os

app = Flask(__name__)

s3 = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",  # ou http://localhost:9000 se for rodar sem Docker Compose
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "minioadmin"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "minioadmin"),
)

@app.route("/")
def home():
    return "API online!"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    s3.upload_fileobj(file, "meu-bucket", file.filename)
    return f"Arquivo {file.filename} enviado com sucesso!"
