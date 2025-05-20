import os
from dotenv import load_dotenv
from pathlib import Path

# Carrega as variáveis de ambiente
load_dotenv()

# Configurações da API
FB_ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
FB_APP_ID = os.getenv('FB_APP_ID')
FB_APP_SECRET = os.getenv('FB_APP_SECRET')
FB_ACCOUNT_ID = os.getenv('FB_ACCOUNT_ID')

# Configurações do projeto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
REPORTS_DIR = PROJECT_ROOT / 'reports'
LOGS_DIR = PROJECT_ROOT / 'logs'

# Cria os diretórios se não existirem
for directory in [DATA_DIR, REPORTS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Configurações de métricas
METRICS = [
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
    'cost_per_conversion',
    'frequency',
    'unique_clicks',
    'unique_ctr',
    'social_reach',
    'social_impressions',
    'video_p25_watched_actions',
    'video_p50_watched_actions',
    'video_p75_watched_actions',
    'video_p95_watched_actions',
    'video_play_actions',
    'video_watch_actions',
    'landing_page_views',
    'onsite_conversion.messaging_first_reply',
    'onsite_conversion.messaging_conversation_started_7d',
    'onsite_conversion.messaging_block',
    'onsite_conversion.messaging_unblock',
    'onsite_conversion.messaging_opt_out',
    'onsite_conversion.messaging_opt_in',
    'onsite_conversion.messaging_first_reply_rate',
    'onsite_conversion.messaging_conversation_started_rate_7d',
    'onsite_conversion.messaging_block_rate',
    'onsite_conversion.messaging_unblock_rate',
    'onsite_conversion.messaging_opt_out_rate',
    'onsite_conversion.messaging_opt_in_rate'
]

# Configurações de período padrão
DEFAULT_DAYS = 30

# Configurações de formatação
CURRENCY_FORMAT = 'R$ {:,.2f}'
PERCENTAGE_FORMAT = '{:.2%}'
NUMBER_FORMAT = '{:,.0f}' 