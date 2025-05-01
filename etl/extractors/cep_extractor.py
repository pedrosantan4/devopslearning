import requests
import logging

class CEPExtractor:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.logger = logging.getLogger(__name__)
    
    def extract_cep_data(self, cep):
        """
        Extrai dados de um CEP
        
        Args:
            cep (str): CEP no formato 00000000
            
        Returns:
            dict: Dicionário com os dados do CEP
        """
        try:
            # Remove caracteres não numéricos
            cep = ''.join(filter(str.isdigit, cep))
            
            url = f"{self.base_url}/{cep}/json"
            self.logger.info(f"Extraindo dados do CEP: {cep}")
            
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            
            if 'erro' in data:
                self.logger.warning(f"CEP {cep} não encontrado")
                return {}
            
            self.logger.info("Dados extraídos com sucesso")
            return data
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Erro ao extrair dados: {str(e)}")
            return {}
        except Exception as e:
            self.logger.error(f"Erro inesperado: {str(e)}")
            return {} 