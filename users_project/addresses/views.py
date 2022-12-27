from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Address


# Create your views here.
def api(request):
    users = []
    type = []
    if 'users' in request.GET:
        users = request.GET.get('users').split(',')
    if 'type' in request.GET:
        type = request.GET.get('type').split(',')
    try:
        q = Address.objects.all()
        if users:
            q = Address.objects.filter(user__in=users)
        if type:
            q = q.filter(type__in=type)
    except Exception as e:
        return JsonResponse({'error': e})
    return JsonResponse({'data': list(q.values())})

def home(request):
    base_url = 'api/v1/addresses'
    query_string = ''
    for item in request.GET:
        query_string += item + '=' + request.GET.get(item) + '&'
    url = f'{base_url}?{query_string}' if query_string else base_url
    return redirect(url)