from django.shortcuts import render
from .models import Squirrel

def map(request):
    squirrels=Squirrel.objects.all()[:50]
    context={
        'squirrels':squirrels,
    }
    return render(request, 'squirrel/map.html', context)
