import pandas as pd
import json
import os
from typing import List, Dict
import logging

class CEPFinder:
    def __init__(self, config_file: str = "config/ceps.json"):
        self.logger = logging.getLogger(__name__)
        self.config_file = config_file
        self.ceps_by_state = self._load_ceps()
    
    def _load_ceps(self) -> dict:
        """
        Carrega CEPs do arquivo de configuração
        
        Returns:
            dict: Dicionário com CEPs por estado
        """
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            else:
                self.logger.warning(f"Arquivo de configuração não encontrado: {self.config_file}")
                return self._get_default_ceps()
        except Exception as e:
            self.logger.error(f"Erro ao carregar CEPs: {str(e)}")
            return self._get_default_ceps()
    
    def _get_default_ceps(self) -> dict:
        """
        Retorna lista padrão de CEPs
        
        Returns:
            dict: Dicionário com CEPs padrão por estado
        """
        return {
            'SP': [
                {
                    'nome': 'São Paulo - Centro',
                    'cep': '01001000'
                },
                {
                    'nome': 'Campinas - Centro',
                    'cep': '13010000'
                },
                {
                    'nome': 'Santos - Centro',
                    'cep': '11010000'
                }
            ],
            'RJ': [
                {
                    'nome': 'Rio de Janeiro - Centro',
                    'cep': '20010000'
                },
                {
                    'nome': 'Niterói - Centro',
                    'cep': '24020000'
                }
            ]
        }
    
    def find_ceps_by_state(self, uf: str) -> pd.DataFrame:
        """
        Encontra CEPs por estado
        
        Args:
            uf (str): Sigla do estado (ex: 'SP', 'RJ')
            
        Returns:
            pd.DataFrame: DataFrame com informações dos CEPs
        """
        uf = uf.upper()
        if uf not in self.ceps_by_state:
            self.logger.warning(f"Estado {uf} não suportado")
            return pd.DataFrame()
        
        df = pd.DataFrame(self.ceps_by_state[uf])
        return df
    
    def add_cep(self, uf: str, nome: str, cep: str) -> bool:
        """
        Adiciona um novo CEP à lista
        
        Args:
            uf (str): Sigla do estado
            nome (str): Nome do local
            cep (str): CEP no formato 00000000
            
        Returns:
            bool: True se o CEP foi adicionado com sucesso
        """
        try:
            uf = uf.upper()
            if uf not in self.ceps_by_state:
                self.ceps_by_state[uf] = []
            
            # Verifica se o CEP já existe
            for cep_info in self.ceps_by_state[uf]:
                if cep_info['cep'] == cep:
                    self.logger.warning(f"CEP {cep} já existe para {uf}")
                    return False
            
            # Adiciona novo CEP
            self.ceps_by_state[uf].append({
                'nome': nome,
                'cep': cep
            })
            
            # Salva no arquivo de configuração
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.ceps_by_state, f, indent=4)
            
            self.logger.info(f"CEP {cep} adicionado com sucesso para {uf}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao adicionar CEP: {str(e)}")
            return False

if __name__ == "__main__":
    finder = CEPFinder()
    
    # Exemplo: encontrar CEPs em São Paulo
    sp_ceps = finder.find_ceps_by_state('SP')
    print("\nCEPs em São Paulo:")
    print(sp_ceps)
    
    # Exemplo: encontrar CEPs no Rio de Janeiro
    rj_ceps = finder.find_ceps_by_state('RJ')
    print("\nCEPs no Rio de Janeiro:")
    print(rj_ceps) 