python
     from django.test import TestCase
     from ..models import Currency, ExchangeRate

     class CurrencyModelTest(TestCase):
         def setUp(self):
             self.usd = Currency.objects.create(code='USD')
             self.eur = Currency.objects.create(code='EUR')

         def test_currency_creation(self):
             self.assertEqual(str(self.usd), 'USD')
             self.assertEqual(str(self.eur), 'EUR')

     class ExchangeRateModelTest(TestCase):
         def setUp(self):
             self.usd = Currency.objects.create(code='USD')
             self.eur = Currency.objects.create(code='EUR')
             self.rate = ExchangeRate.objects.create(from_currency=self.usd, to_currency=self.eur, rate=1.2)

         def test_exchange_rate_creation(self):
             self.assertEqual(str(self.rate), '1.2 USD to EUR')
     
