from django.shortcuts import render
from django.http import JsonResponse
from .models import Order

# Create your views here.
def api(request):
    q = Order.objects.all()
    for param in request.GET:
        q = q.filter(**{param: request.GET[param]})
    return JsonResponse({'orders': list(q.values())})