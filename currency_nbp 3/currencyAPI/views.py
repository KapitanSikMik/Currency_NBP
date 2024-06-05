from django.http import JsonResponse
from .models import Currency
import requests
from datetime import datetime, timedelta

def get_rates(request):
    current_date = datetime.now().date()
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=30)
    url = f"http://api.nbp.pl/api/exchangerates/tables/A/{start_date}/{end_date}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    data = response.json()
    rates_data = []
    for item in data[0]['rates']:
        rates_data.append({
            'code': item['code'], 'rate': item['mid'], 'date': data[0]['effectiveDate']
        })
        old_currency = Currency.objects.filter(code=item['code'], date=current_date).first()
        if not old_currency:
            currency = Currency(code=item['code'], rate=item['mid'], date=current_date)
            currency.save()

    return JsonResponse({'status': 'success', 'data': rates_data})
