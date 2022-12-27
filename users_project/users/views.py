from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
def api(request):
    ids = []
    fields = []

    if 'username' in request.GET:
        value = request.GET['username']
        q = User.objects.get(username=value).id
        return JsonResponse({'id': q})

        
    if 'fields' in request.GET:
        fields = request.GET.get('fields').split(',')
    if 'id' in request.GET:
        ids = request.GET.get('id').split(',')
    try:
        if ids:
            q = User.objects.filter(id__in=ids).values(*fields)
        else:
            q = User.objects.all().values()
    except Exception as e:
        return JsonResponse({'error': e})

    return JsonResponse({'data': q})

def home(request):
    base_url = 'api/v1/users'
    query_string = ''
    for item in request.GET:
        query_string += item + '=' + request.GET.get(item) + '&'
    url = f'{base_url}?{query_string}' if query_string else base_url
    return redirect(url)