from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.append('/opt/airflow/project')

from etl.extractors.cep_extractor import CEPExtractor
from etl.transformers.cep_transformer import CEPTransformer
from etl.loaders.cep_loader import CEPLoader
from etl.utils.cep_finder import CEPFinder

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,  # Sem retentativas
    'retry_delay': timedelta(seconds=10),  # Delay menor
    'execution_timeout': timedelta(seconds=30),  # Timeout de 30 segundos
}

dag = DAG(
    'cep_etl',
    default_args=default_args,
    description='ETL para dados de CEPs',
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1  # Apenas uma execução por vez
)

def run_etl(**context):
    # Inicializa os componentes
    cep_finder = CEPFinder()
    extractor = CEPExtractor()
    transformer = CEPTransformer()
    loader = CEPLoader()
    
    # Obtém apenas 3 CEPs de SP para teste rápido
    ceps = cep_finder.find_ceps_by_state('SP').head(3)
    if ceps.empty:
        print("Nenhum CEP encontrado para o estado SP")
        return
    
    print(f"Processando {len(ceps)} CEPs")
    
    # Lista para armazenar todos os dados
    all_data = []
    
    # Processa cada CEP
    for _, cep_info in ceps.iterrows():
        try:
            cep = cep_info['cep']
            nome = cep_info['nome']
            
            print(f"Processando CEP: {cep} ({nome})")
            
            # Extrai dados
            raw_data = extractor.extract_cep_data(cep)
            
            if not raw_data:
                print(f"Nenhum dado encontrado para o CEP {cep}")
                continue
            
            # Adiciona informações do local
            raw_data['nome_local'] = nome
            all_data.append(raw_data)
            
        except Exception as e:
            print(f"Erro ao processar CEP {cep}: {str(e)}")
            continue
    
    if not all_data:
        print("Nenhum dado coletado para processar")
        return
    
    # Transforma os dados
    print("Transformando dados...")
    df = transformer.transform_batch(all_data)
    
    if df.empty:
        print("Nenhum dado válido após transformação")
        return
    
    # Carrega os dados
    print("Carregando dados...")
    if not loader.load_data(df):
        print("Falha ao carregar dados")
        return
    
    print("ETL concluído com sucesso!")

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    provide_context=True,
    dag=dag,
)