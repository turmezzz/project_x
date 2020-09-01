from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        return HttpResponse('ok', content_type="text/plain")
    return render(request, 'home.html', {})
