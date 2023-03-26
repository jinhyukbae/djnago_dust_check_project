from django.shortcuts import render
from .api import check_air

def index(request):
    res = check_air()
    pm10 = res.get('가양동')
    context = {'station': '강서구', 'pm10': pm10}
    return render(request, 'dust_checker/dust_main.html', context)

def detail(request):
    res = check_air()
    context = {'dust': res}
    return render(request, 'dust_checker/dust_detail.html', context)