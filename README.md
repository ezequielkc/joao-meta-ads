# Meta Ads Analytics 📊

Este projeto é uma ferramenta poderosa para análise de anúncios da Meta (Facebook), permitindo coletar dados através da API oficial e gerar relatórios detalhados com métricas de performance dos seus anúncios.

## 🎯 Visão Geral

O Meta Ads Analytics é uma solução completa que:
- Coleta dados automaticamente da API do Facebook
- Processa e analisa métricas importantes
- Gera relatórios em Excel e dashboards interativos
- Fornece visualizações gráficas das campanhas
- Mantém um histórico de performance

## 📁 Estrutura do Projeto

```
meta-ads-analytics/
├── src/                    # Código fonte principal
│   ├── api.py             # Integração com a API do Facebook
│   ├── processor.py       # Processamento de dados
│   ├── visualizer.py      # Geração de gráficos e dashboards
│   └── config.py          # Configurações do projeto
├── data/                  # Armazenamento de dados brutos
├── reports/              # Relatórios gerados
├── logs/                 # Logs do sistema
├── tests/                # Testes automatizados
├── docs/                 # Documentação adicional
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
└── .env                 # Configurações de ambiente
```

## 📋 Guia de Instalação e Uso

### 1. Pré-requisitos

Antes de começar, você precisa ter:
- Python 3.8 ou superior instalado
- Uma conta de desenvolvedor do Facebook
- Uma conta de anúncios do Facebook ativa
- Acesso à API do Facebook Ads

### 2. Configuração do Ambiente

1. **Clone o repositório**
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd meta-ads-analytics
   ```

2. **Crie um ambiente virtual**
   ```bash
   # No Windows
   python -m venv venv
   venv\Scripts\activate

   # No Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configuração da API do Facebook

1. **Acesse o Facebook for Developers**
   - Vá para [developers.facebook.com](https://developers.facebook.com)
   - Faça login com sua conta

2. **Crie um novo aplicativo**
   - Clique em "Criar App"
   - Selecione "Business" como tipo
   - Preencha as informações básicas

3. **Configure o Marketing API**
   - No painel do app, vá para "Adicionar Produtos"
   - Adicione o produto "Marketing API"
   - Siga as instruções de configuração

4. **Obtenha as credenciais necessárias**

   a. **App ID e App Secret**
   - Vá para Configurações > Básico
   - Copie o App ID e App Secret

   b. **Access Token**
   - Vá para Ferramentas > Graph API Explorer
   - Selecione seu aplicativo
   - Clique em "Gerar Token de Acesso"
   - Selecione as permissões:
     - `ads_read`
     - `ads_management`
     - `read_insights`

   c. **Account ID**
   - Acesse o [Facebook Ads Manager](https://business.facebook.com/adsmanager)
   - O ID da conta está na URL ou nas configurações

### 4. Configuração do Projeto

1. **Crie o arquivo de ambiente**
   - Copie o arquivo `.env.example` para `.env`
   - Preencha com suas credenciais:
   ```env
   # Credenciais do Facebook
   FB_ACCESS_TOKEN=seu_token_de_acesso
   FB_APP_ID=seu_app_id
   FB_APP_SECRET=seu_app_secret
   FB_ACCOUNT_ID=seu_account_id

   # Configurações do Projeto
   DEBUG=True
   LOG_LEVEL=INFO
   REPORT_DAYS=30

   # Configurações de Cache
   ENABLE_CACHE=True
   CACHE_EXPIRY=3600

   # Configurações de Relatório
   REPORT_FORMAT=xlsx
   INCLUDE_GRAPHS=True
   SAVE_RAW_DATA=True

   # Configurações da API
   API_VERSION=v18.0
   REQUEST_TIMEOUT=30
   MAX_RETRIES=3
   ```

### 5. Executando o Projeto

1. **Execute o script principal**
   ```bash
   python main.py
   ```

2. **Verifique os resultados**
   - Relatórios Excel: pasta `reports/`
   - Dashboards HTML: pasta `reports/`
   - Logs: pasta `logs/`

### 6. Entendendo os Relatórios

O projeto gera vários tipos de relatórios:

1. **Relatório Excel**
   - Dados brutos de todos os anúncios
   - Resumo das métricas principais
   - Performance por campanha
   - Tendências diárias

2. **Dashboard Interativo**
   - Gráficos de tendências
   - Comparação entre campanhas
   - Análise de ROI
   - Métricas em tempo real

3. **Gráficos de Comparação**
   - Comparação entre campanhas
   - Análise de ROI por campanha
   - Tendências de performance

### 7. Solução de Problemas Comuns

1. **Erro de Autenticação**
   - Verifique se o token de acesso é válido
   - Confirme se as credenciais estão corretas
   - Verifique as permissões do token
   - Solução: Gere um novo token de acesso

2. **Erro de API**
   - Verifique os logs em `logs/`
   - Confirme se a conta tem acesso à API
   - Verifique o rate limiting
   - Solução: Aumente o intervalo entre requisições

3. **Erro de Dados**
   - Verifique se há dados no período
   - Confirme se as métricas estão disponíveis
   - Verifique os logs de processamento
   - Solução: Ajuste o período de análise

### 8. Personalização

1. **Adicionar Novas Métricas**
   ```python
   # Em src/config.py
   METRICS = {
       'impressions': 'Impressões',
       'clicks': 'Cliques',
       'spend': 'Gasto',
       'reach': 'Alcance',
       'cpc': 'CPC',
       'ctr': 'CTR',
       'cpm': 'CPM',
       'conversions': 'Conversões',
       'nova_metrica': 'Nova Métrica'  # Adicione aqui
   }
   ```

2. **Modificar Período**
   ```python
   # No arquivo .env
   REPORT_DAYS=60  # Altere para o número de dias desejado
   ```

3. **Personalizar Relatórios**
   ```python
   # Em src/visualizer.py
   def create_custom_chart(data, metric):
       # Implemente sua visualização personalizada
       pass
   ```

## 📊 Métricas Disponíveis

### Métricas Básicas
- Impressões: Número de vezes que seu anúncio foi exibido
- Cliques: Número de cliques no anúncio
- Gasto: Valor total gasto na campanha
- Alcance: Número de pessoas únicas que viram o anúncio
- CPC: Custo por clique
- CTR: Taxa de cliques
- CPM: Custo por mil impressões
- Conversões: Número de conversões geradas

### Métricas Avançadas
- Frequência: Média de impressões por pessoa
- Cliques Únicos: Número de pessoas que clicaram
- CTR Único: Taxa de cliques únicos
- Métricas de Vídeo: Visualizações, retenção
- Métricas de Mensagens: Respostas, taxa de resposta
- Métricas de Landing Page: Tempo na página, bounce rate

## 🔄 Atualizações

Para manter o projeto atualizado:

1. **Atualizar Dependências**
   ```bash
   pip install -r requirements.txt --upgrade
   ```

2. **Atualizar Código**
   ```bash
   git pull origin main
   ```

3. **Verificar Novas Funcionalidades**
   - Consulte a documentação em `docs/`
   - Verifique as issues no repositório
   - Acompanhe as atualizações da API

## 📝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça commit das mudanças
   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie um pull request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Suporte

Se você encontrar algum problema ou tiver alguma dúvida:
1. Verifique a documentação em `docs/`
2. Abra uma issue no GitHub
3. Entre em contato através do email de suporte # joao-meta-ads
