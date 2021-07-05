from django.shortcuts import render
from .models import production_pvrmt
from django.http import JsonResponse

# Create your views here.
def production(request):

	temps = []
	stockage = []

	productionpvrmt = production_pvrmt.objects.order_by('-dt_utc')[:500]
	for prod in productionpvrmt :
		temps.append(prod.dt_utc)
		stockage.append(prod.Charge)


	return render(request, 'blog/production.html', {'productionpvrmt' : productionpvrmt, 'temps' : temps, 'stockage' : stockage, })
