import pandas as pd
from datetime import datetime
import logging

class CEPTransformer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.required_fields = ['cep', 'logradouro', 'bairro', 'localidade', 'uf']
    
    def validate_data(self, data: dict) -> bool:
        """
        Valida se os dados do CEP contêm todos os campos necessários
        
        Args:
            data (dict): Dicionário com os dados do CEP
            
        Returns:
            bool: True se os dados são válidos, False caso contrário
        """
        if not data:
            return False
            
        for field in self.required_fields:
            if field not in data or not data[field]:
                self.logger.warning(f"Campo obrigatório ausente: {field}")
                return False
                
        return True
    
    def transform_data(self, data: dict) -> dict:
        """
        Transforma e padroniza os dados do CEP
        
        Args:
            data (dict): Dicionário com os dados brutos do CEP
            
        Returns:
            dict: Dicionário com os dados transformados
        """
        if not self.validate_data(data):
            return {}
            
        try:
            # Cria cópia dos dados
            transformed = data.copy()
            
            # Padroniza o CEP (remove caracteres não numéricos)
            transformed['cep'] = ''.join(filter(str.isdigit, transformed['cep']))
            
            # Adiciona metadados
            transformed['data_extracao'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Padroniza nomes (primeira letra maiúscula)
            for field in ['logradouro', 'bairro', 'localidade']:
                if field in transformed:
                    transformed[field] = transformed[field].title()
            
            return transformed
            
        except Exception as e:
            self.logger.error(f"Erro ao transformar dados: {str(e)}")
            return {}
    
    def transform_batch(self, data_list: list) -> pd.DataFrame:
        """
        Transforma uma lista de dados de CEPs
        
        Args:
            data_list (list): Lista de dicionários com dados de CEPs
            
        Returns:
            pd.DataFrame: DataFrame com os dados transformados
        """
        transformed_data = []
        
        for data in data_list:
            transformed = self.transform_data(data)
            if transformed:
                transformed_data.append(transformed)
        
        if not transformed_data:
            self.logger.warning("Nenhum dado válido após transformação")
            return pd.DataFrame()
            
        return pd.DataFrame(transformed_data) 