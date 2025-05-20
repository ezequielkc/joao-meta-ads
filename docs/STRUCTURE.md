# Estrutura do Projeto Meta Ads Analytics

## 📁 Visão Geral da Estrutura

```
meta-ads-analytics/
├── src/                    # Código fonte do projeto
│   ├── __init__.py        # Inicializador do pacote
│   ├── api.py             # Módulo de integração com a API do Facebook
│   ├── processor.py       # Módulo de processamento de dados
│   ├── visualizer.py      # Módulo de visualização e gráficos
│   └── config.py          # Configurações centralizadas
├── data/                   # Diretório para armazenamento de dados
├── reports/               # Diretório para relatórios gerados
├── logs/                  # Diretório para logs do sistema
├── docs/                  # Documentação do projeto
├── tests/                 # Testes automatizados
├── main.py               # Script principal
├── requirements.txt      # Dependências do projeto
└── README.md            # Documentação principal
```

## 📦 Descrição dos Componentes

### 1. Diretório `src/`

Contém todo o código fonte do projeto, organizado em módulos:

#### `api.py`
- Responsável pela comunicação com a API do Facebook
- Gerencia autenticação e requisições
- Implementa métodos para obter dados de anúncios
- Trata erros de API e rate limiting

#### `processor.py`
- Processa os dados brutos da API
- Calcula métricas derivadas
- Gera resumos e análises
- Prepara dados para visualização

#### `visualizer.py`
- Gera visualizações e gráficos
- Cria dashboards interativos
- Implementa diferentes tipos de relatórios
- Exporta gráficos em vários formatos

#### `config.py`
- Centraliza todas as configurações do projeto
- Gerencia variáveis de ambiente
- Define constantes e parâmetros
- Cria estrutura de diretórios necessária

### 2. Diretórios de Dados

#### `data/`
- Armazena dados brutos da API
- Cache de consultas frequentes
- Arquivos temporários de processamento

#### `reports/`
- Relatórios Excel gerados
- Dashboards HTML
- Gráficos e visualizações
- Arquivos de exportação

#### `logs/`
- Logs de execução
- Registros de erros
- Histórico de operações
- Métricas de performance

### 3. Arquivos Principais

#### `main.py`
- Ponto de entrada do programa
- Orquestra a execução dos módulos
- Gerencia o fluxo de trabalho
- Trata exceções globais

#### `requirements.txt`
Lista todas as dependências do projeto:
- `facebook-business`: API do Facebook
- `pandas`: Processamento de dados
- `plotly`: Visualizações interativas
- `dash`: Dashboards web
- `rich`: Interface no terminal
- Outras bibliotecas de suporte

## 🔄 Fluxo de Dados

1. **Coleta de Dados**
   - `main.py` inicia o processo
   - `api.py` obtém dados da API do Facebook
   - Dados são armazenados temporariamente

2. **Processamento**
   - `processor.py` recebe dados brutos
   - Calcula métricas e indicadores
   - Prepara dados para visualização

3. **Visualização**
   - `visualizer.py` gera relatórios
   - Cria dashboards interativos
   - Exporta gráficos e análises

4. **Armazenamento**
   - Relatórios são salvos em `reports/`
   - Logs são registrados em `logs/`
   - Dados processados podem ser armazenados em `data/`

## ⚙️ Configuração

### Variáveis de Ambiente
O projeto utiliza um arquivo `.env` para configurações sensíveis:
```
FB_ACCESS_TOKEN=seu_token_de_acesso
FB_APP_ID=seu_app_id
FB_APP_SECRET=seu_app_secret
FB_ACCOUNT_ID=seu_account_id
DEBUG=True
LOG_LEVEL=INFO
REPORT_DAYS=30
```

### Configurações do Projeto
Definidas em `src/config.py`:
- Diretórios do projeto
- Métricas a serem coletadas
- Formatos de saída
- Períodos padrão

## 🛠️ Desenvolvimento

### Adicionando Novas Funcionalidades

1. **Novas Métricas**
   - Adicione a métrica em `config.py` (METRICS)
   - Implemente o processamento em `processor.py`
   - Adicione visualização em `visualizer.py`

2. **Novos Relatórios**
   - Crie novo método em `visualizer.py`
   - Adicione opção em `main.py`
   - Atualize documentação

3. **Novas Integrações**
   - Crie novo módulo em `src/`
   - Implemente interface em `api.py`
   - Atualize `requirements.txt`

## 📊 Métricas Disponíveis

### Métricas Básicas
- Impressões
- Cliques
- Gasto
- Alcance
- CPC
- CTR
- CPM
- Conversões

### Métricas Avançadas
- Frequência
- Cliques Únicos
- CTR Único
- Métricas de Vídeo
- Métricas de Mensagens
- Métricas de Landing Page

## 🔍 Solução de Problemas

### Logs
- Verifique `logs/` para detalhes de erros
- Níveis de log configuráveis
- Histórico de execuções

### Debug
- Modo debug ativável via `.env`
- Logs detalhados
- Validação de dados

### Performance
- Cache de dados
- Processamento otimizado
- Rate limiting da API 