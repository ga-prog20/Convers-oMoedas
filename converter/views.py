python
     from django.http import JsonResponse
     from django.views import View
     from .models import ExchangeRate, Currency

     class ConvertCurrencyView(View):
         def get(self, request):
             from_currency_code = request.GET.get('from')
             to_currency_code = request.GET.get('to')
             amount = float(request.GET.get('amount', 0))

             try:
                 from_currency = Currency.objects.get(code=from_currency_code)
                 to_currency = Currency.objects.get(code=to_currency_code)
                 exchange_rate = ExchangeRate.objects.get(from_currency=from_currency, to_currency=to_currency)
                 converted_amount = amount * exchange_rate.rate
                 return JsonResponse({'converted_amount': converted_amount})
             except (Currency.DoesNotExist, ExchangeRate.DoesNotExist):
                 return JsonResponse({'error': 'Invalid currency codes'})
