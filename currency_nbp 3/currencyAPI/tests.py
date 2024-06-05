from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from .models import Currency
import requests
from datetime import datetime  # Import datetime

class GetRatesViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('requests.get')
    def test_get_rates_success(self, mock_get):
        mock_response_data = [{
            'table': 'A',
            'no': '101/A/NBP/2022',
            'effectiveDate': '2023-01-01',
            'rates': [
                {'currency': 'dollar', 'code': 'USD', 'mid': 3.75},
                {'currency': 'euro', 'code': 'EUR', 'mid': 4.50}
            ]
        }]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        response = self.client.get(reverse('get_rates'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['data']), 2)
        self.assertEqual(response.json()['data'][0]['code'], 'USD')
        self.assertEqual(response.json()['data'][1]['code'], 'EUR')

        # Check if data is saved in the database
        self.assertEqual(Currency.objects.count(), 2)
        usd = Currency.objects.get(code='USD')
        self.assertEqual(usd.rate, 3.75)
        eur = Currency.objects.get(code='EUR')
        self.assertEqual(eur.rate, 4.50)

    @patch('requests.get')
    def test_get_rates_api_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = requests.HTTPError()

        response = self.client.get(reverse('get_rates'))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json()['status'], 'error')

    @patch('requests.get')
    def test_get_rates_existing_currency(self, mock_get):
        # Create a currency entry to test for duplication
        Currency.objects.create(code='USD', rate=3.75, date=datetime.now().date())

        mock_response_data = [{
            'table': 'A',
            'no': '101/A/NBP/2022',
            'effectiveDate': '2023-01-01',
            'rates': [
                {'currency': 'dollar', 'code': 'USD', 'mid': 3.75},
                {'currency': 'euro', 'code': 'EUR', 'mid': 4.50}
            ]
        }]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        response = self.client.get(reverse('get_rates'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Currency.objects.count(), 2)  # No new USD entry
