import os
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
import pandas as pd
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def initialize_api():
    """Inicializa a API do Facebook com as credenciais."""
    FacebookAdsApi.init(
        access_token=os.getenv('FB_ACCESS_TOKEN'),
        app_id=os.getenv('FB_APP_ID'),
        app_secret=os.getenv('FB_APP_SECRET')
    )

def get_ad_insights(account_id, days=30):
    """Obtém insights dos anúncios para o período especificado."""
    account = AdAccount(f'act_{account_id}')
    
    # Define o período de análise
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Parâmetros para a consulta
    params = {
        'time_range': {
            'since': start_date.strftime('%Y-%m-%d'),
            'until': end_date.strftime('%Y-%m-%d')
        },
        'fields': [
            'campaign_name',
            'adset_name',
            'ad_name',
            'impressions',
            'clicks',
            'spend',
            'reach',
            'cpc',
            'ctr',
            'cpm',
            'conversions',
            'cost_per_conversion'
        ],
        'level': 'ad'
    }
    
    # Faz a requisição à API
    insights = account.get_insights(params=params)
    return list(insights)

def generate_report(insights):
    """Gera um relatório em Excel com os dados dos anúncios."""
    # Converte os insights para um DataFrame
    df = pd.DataFrame(insights)
    
    # Calcula métricas adicionais
    df['ROI'] = (df['conversions'] * 100) / df['spend'].replace(0, 1)
    
    # Formata as colunas numéricas
    numeric_columns = ['spend', 'cpc', 'cpm', 'cost_per_conversion']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Gera o nome do arquivo com timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'meta_ads_report_{timestamp}.xlsx'
    
    # Salva o relatório em Excel
    df.to_excel(filename, index=False)
    print(f'Relatório gerado com sucesso: {filename}')
    
    # Imprime um resumo das métricas principais
    print("\nResumo das métricas principais:")
    print(f"Total de impressões: {df['impressions'].sum():,.0f}")
    print(f"Total de cliques: {df['clicks'].sum():,.0f}")
    print(f"Total gasto: R$ {df['spend'].sum():,.2f}")
    print(f"CTR médio: {df['ctr'].mean():.2%}")
    print(f"CPC médio: R$ {df['cpc'].mean():,.2f}")
    print(f"Conversões totais: {df['conversions'].sum():,.0f}")

def main():
    try:
        # Inicializa a API
        initialize_api()
        
        # Obtém o ID da conta dos anúncios
        account_id = os.getenv('FB_ACCOUNT_ID')
        
        # Obtém os insights dos anúncios
        print("Obtendo dados dos anúncios...")
        insights = get_ad_insights(account_id)
        
        # Gera o relatório
        generate_report(insights)
        
    except Exception as e:
        print(f"Erro ao executar o script: {str(e)}")

if __name__ == "__main__":
    main() 