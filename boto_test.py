import boto3

# Configuração do cliente do MinIO
s3_client = boto3.client(
    's3',
    endpoint_url='http://minio:9000',  # URL do MinIO usando o nome do serviço
    aws_access_key_id='minioadmin',  # Chaves do MinIO
    aws_secret_access_key='minioadmin',
    region_name='us-east-1'
)

# Teste para listar buckets
response = s3_client.list_buckets()
print("Buckets disponíveis:", response['Buckets'])

# Criar um novo bucket
bucket_name = 'meu-bucket-test'
s3_client.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' criado!")

# Fazer upload de um arquivo de teste
with open('teste.txt', 'w') as file:
    file.write("Este é um arquivo de teste para o MinIO!")

s3_client.upload_file('teste.txt', bucket_name, 'teste.txt')
print("Arquivo enviado com sucesso!")

# Listar objetos no bucket
objects = s3_client.list_objects(Bucket=bucket_name)
print("Objetos no bucket:", objects['Contents'])
