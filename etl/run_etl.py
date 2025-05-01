from extractors.cep_extractor import CEPExtractor
from transformers.cep_transformer import CEPTransformer
from loaders.cep_loader import CEPLoader
from utils.cep_finder import CEPFinder
import logging
import sys

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('etl.log')
    ]
)
logger = logging.getLogger(__name__)

def run_etl():
    try:
        # Inicializa componentes
        logger.info("Inicializando componentes do ETL...")
        cep_finder = CEPFinder()
        extractor = CEPExtractor()
        transformer = CEPTransformer()
        loader = CEPLoader()
        
        # Obtém CEPs de SP
        ceps = cep_finder.find_ceps_by_state('SP')
        if ceps.empty:
            logger.error("Nenhum CEP encontrado para o estado SP")
            return
            
        logger.info(f"Encontrados {len(ceps)} CEPs em SP")
        
        # Lista para armazenar todos os dados
        all_data = []
        
        # Processa cada CEP
        for _, cep_info in ceps.iterrows():
            try:
                cep = cep_info['cep']
                nome = cep_info['nome']
                
                logger.info(f"Processando CEP: {cep} ({nome})")
                
                # Extrai dados
                raw_data = extractor.extract_cep_data(cep)
                
                if not raw_data:
                    logger.warning(f"Nenhum dado encontrado para o CEP {cep}")
                    continue
                
                # Adiciona informações do local
                raw_data['nome_local'] = nome
                
                all_data.append(raw_data)
                
            except Exception as e:
                logger.error(f"Erro ao processar CEP {cep}: {str(e)}", exc_info=True)
                continue
        
        if not all_data:
            logger.error("Nenhum dado coletado para processar")
            return
            
        # Transforma os dados
        logger.info("Transformando dados...")
        df = transformer.transform_batch(all_data)
        
        if df.empty:
            logger.error("Nenhum dado válido após transformação")
            return
            
        # Carrega os dados
        logger.info("Carregando dados...")
        if not loader.load_data(df):
            logger.error("Falha ao carregar dados")
            return
        
        logger.info("ETL concluído com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro no processo ETL: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    run_etl() 