import unittest
from unittest.mock import patch, MagicMock
from src.api import FacebookAdsAPI

class TestFacebookAdsAPI(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste."""
        self.api = FacebookAdsAPI()

    @patch('facebook_business.api.FacebookAdsApi.init')
    def test_initialization(self, mock_init):
        """Testa a inicialização da API."""
        self.api = FacebookAdsAPI()
        mock_init.assert_called_once()

    @patch('facebook_business.adobjects.adaccount.AdAccount.get_insights')
    def test_get_ad_insights(self, mock_get_insights):
        """Testa a obtenção de insights dos anúncios."""
        # Configura o mock
        mock_data = [
            {
                'campaign_name': 'Test Campaign',
                'impressions': 1000,
                'clicks': 100,
                'spend': 50.0
            }
        ]
        mock_get_insights.return_value = mock_data

        # Executa o teste
        insights = self.api.get_ad_insights(days=7)

        # Verifica os resultados
        self.assertEqual(len(insights), 1)
        self.assertEqual(insights[0]['campaign_name'], 'Test Campaign')
        self.assertEqual(insights[0]['impressions'], 1000)

    @patch('facebook_business.adobjects.adaccount.AdAccount.api_get')
    def test_get_account_info(self, mock_api_get):
        """Testa a obtenção de informações da conta."""
        # Configura o mock
        mock_data = {
            'name': 'Test Account',
            'currency': 'BRL',
            'timezone_name': 'America/Sao_Paulo'
        }
        mock_api_get.return_value = mock_data

        # Executa o teste
        account_info = self.api.get_account_info()

        # Verifica os resultados
        self.assertEqual(account_info['name'], 'Test Account')
        self.assertEqual(account_info['currency'], 'BRL')

if __name__ == '__main__':
    unittest.main() 