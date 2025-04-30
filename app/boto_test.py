import boto3
from botocore.exceptions import NoCredentialsError, EndpointConnectionError

try:
    s3 = boto3.client(
        's3',
        endpoint_url='http://minio:9000',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin',
        region_name='us-east-1',
    )

    response = s3.list_buckets()
    print("Buckets existentes:", response['Buckets'])

    bucket_name = 'meu-bucket-test'
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' criado com sucesso!")

except NoCredentialsError:
    print("Credenciais inválidas.")
except EndpointConnectionError as e:
    print("Erro de conexão com o MinIO:", str(e))
except Exception as e:
    print("Erro:", str(e))

