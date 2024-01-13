 python
     from django.test import TestCase
     from django.urls import reverse
     from ..models import Currency, ExchangeRate

     class ConvertCurrencyViewTest(TestCase):
         def setUp(self):
             self.usd = Currency.objects.create(code='USD')
             self.eur = Currency.objects.create(code='EUR')
             self.rate = ExchangeRate.objects.create(from_currency=self.usd, to_currency=self.eur, rate=1.2)

         def test_convert_currency_view(self):
             url = reverse('convert_currency')
             response = self.client.get(url, {'from': 'USD', 'to': 'EUR', 'amount': 100})
             self.assertEqual(response.status_code, 200)
             self.assertEqual(response.json()['converted_amount'], 120.0)
