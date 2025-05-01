import boto3
import pandas as pd
from datetime import datetime
import logging

class CEPLoader:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.s3 = boto3.client(
            "s3",
            endpoint_url="http://minio:9000",  # Nome do serviço MinIO
            aws_access_key_id="minioadmin",
            aws_secret_access_key="minioadmin",
            verify=False
        )
    
    def load_data(self, df: pd.DataFrame, bucket: str = "cep-data") -> bool:
        """
        Carrega os dados para o MinIO
        
        Args:
            df (pd.DataFrame): DataFrame com os dados a serem carregados
            bucket (str): Nome do bucket no MinIO
            
        Returns:
            bool: True se o carregamento foi bem sucedido, False caso contrário
        """
        try:
            if df.empty:
                self.logger.error("DataFrame vazio, nada para carregar")
                return False
                
            # Converte para CSV
            csv_buffer = df.to_csv(index=False).encode()
            
            # Define nome do arquivo no formato: YYYYMMDD_cep_data.csv
            file_name = f"{datetime.now().strftime('%Y%m%d')}_cep_data.csv"
            
            # Upload para MinIO
            self.logger.info(f"Fazendo upload dos dados para o MinIO: {file_name}")
            
            # Cria o bucket se não existir
            try:
                self.s3.head_bucket(Bucket=bucket)
            except:
                self.logger.info(f"Criando bucket: {bucket}")
                self.s3.create_bucket(Bucket=bucket)
            
            self.s3.put_object(
                Bucket=bucket,
                Key=f"raw/{file_name}",
                Body=csv_buffer
            )
            
            self.logger.info("Dados carregados com sucesso!")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar dados: {str(e)}", exc_info=True)
            return False 