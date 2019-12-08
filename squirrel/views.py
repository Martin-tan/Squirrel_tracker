from django.shortcuts import render
from .models import Squirrel
import numpy as np
from django.http import HttpResponse
from django.http import Http404

def map(request):
    squirrels=Squirrel.objects.all()[:50]
    context={
        'squirrels':squirrels,
    }
    return render(request, 'squirrel/map.html', context)

def all_squirrels(request):
    squirrel_list = Squirrel.objects.all()[::-1][:5]
    context = {'squirrel_list': squirrel_list}
    return render(request, 'squirrel/index.html', context)

def squirrel_details(request, squirrel_id):
    try:         #squirrel not found
        squirrel = Squirrel.objects.get(Unique_Squirrel_ID = squirrel_id)
        delete = request.POST.get('Delete')
        update = request.POST.get('Update')
        if delete == 'delete':
            squirrel.delete()
            return redirect('')
        if update == 'update':
            squirrel.Latitude = request.POST.get('Latitude')
            squirrel.Longitude = request.POST.get('Longitude')
            id = request.POST.get('Unique_Squirrel_ID')
            if id in [i.Unique_Squirrel_ID for i in Squirrel.objects.all()]:
                raise Http404("UNIQUE ID CONSTRAINT failed!")
            else:
                squirrel.Unique_Squirrel_ID = id
            squirrel.Shift = request.POST.get('Shift')
            squirrel.Date = request.POST.get('Date')
            squirrel.Age = request.POST.get('Age')
            squirrel.Primary_Fur_Color = request.POST.get('Primary_Fur_Color')
            squirrel.Location = request.POST.get('Location')
            squirrel.Specific_Location = request.POST.get('Specific_Location')
            squirrel.Running = request.POST.get('Running')
            squirrel.Chasing = request.POST.get('Chasing')
            squirrel.Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID')
            squirrel.Climbing = request.POST.get('Climbing')
            squirrel.Eating = request.POST.get('Eating')
            squirrel.Foraging = request.POST.get('Foraging')
            squirrel.Other_Activities = request.POST.get('Other_Activities')
            squirrel.Kuks = request.POST.get('Kuks')
            squirrel.Quaas = request.POST.get('Quaas')
            squirrel.Moans = request.POST.get('Moans')
            squirrel.Tail_flags = request.POST.get('Tail_flags')
            squirrel.Tail_twitches = request.POST.get('Tail_twitches')
            squirrel.Approaches = request.POST.get('Approaches')
            squirrel.Indifferent = request.POST.get('Indifferent')
            squirrel.Runs_from = request.POST.get('Runs_from')
            squirrel.save()
            return redirect('')
        return render(request, 'squirrel/detail.html',{'squirrel':squirrel})
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel does not exist")

def add_squirrels(request):
    if request.method == 'POST':
        latitude = request.POST.get('Latitude')
        longitude = request.POST.get('Longitude')
        unique_squirrel_id = request.POST.get('Unique_Squirrel_ID')
        if unique_squirrel_id in [i.Unique_Squirrel_ID for i in Squirrel.objects.all()]:
            raise Http404("UNIQUE ID CONSTRAINT failed!")
        shift = request.POST.get('Shift')
        date = request.POST.get('Date')
        age = request.POST.get('Age')
        primary_fur_color = request.POST.get('Primary_Fur_Color')
        location = request.POST.get('Location')
        specific_location = request.POST.get('Specific_Location')
        running = request.POST.get('Running')
        chasing = request.POST.get('Chasing')
        climbing = request.POST.get('Climbing')
        eating = request.POST.get('Eating')
        foraging = request.POST.get('Foraging')
        other_activities = request.POST.get('Other_Activities')
        kuks = request.POST.get('Kuks')
        quaas = request.POST.get('Quaas')
        moans = request.POST.get('Moans')
        tail_flags = request.POST.get('Tail_flags')
        tail_twitches = request.POST.get('Tail_twitches')
        approaches = request.POST.get('Approaches')
        indifferent = request.POST.get('Indifferent')
        runs_from = request.POST.get('Runs_from')
        Squirrel.objects.create(
            Latitude = latitude,
            Longitude = longitude,
            Unique_Squirrel_ID = unique_squirrel_id,
            Shift = shift,
            Date = date,
            Age = age,
            Primary_Fur_Color = primary_fur_color,
            Location = location,
            Specific_Location = specific_location,
            Running = running,
            Chasing = chasing,
            Climbing = climbing,
            Eating = eating,
            Foraging = foraging,
            Other_Activities = other_activities,
            Kuks = kuks,
            Quaas = quaas,
            Moans = moans,
            Tail_flags = tail_flags,
            Tail_twitches = tail_twitches,
            Approaches = approaches,
            Indifferent = indifferent,
            Runs_from = runs_from
        )
    return render(request, 'squirrel/add.html')

def squirrel_stats(request):
    squirrel_list = Squirrel.objects.all()
    running_rate_list = []
    age = {}
    fur_color = {}
    for i in squirrel_list:
        if i.Age!='':
            age[i.Age] = age.get(i.Age,0) + 1
        if i.Primary_Fur_Color!='':
            fur_color[i.Primary_Fur_Color] = fur_color.get(i.Primary_Fur_Color,0) + 1
        if i.Running == 'True':
            running_rate_list.append(True)
        elif i.Running == 'False':
            running_rate_list.append(False)

    mean_latitude = np.mean([i.Latitude for i in squirrel_list if i.Latitude])
    max_latitude = np.max([i.Latitude for i in squirrel_list if i.Latitude])
    min_latitude = np.min([i.Latitude for i in squirrel_list if i.Latitude])
    mean_longitude = np.mean([i.Longitude for i in squirrel_list if i.Longitude])
    max_longitude = np.max([i.Longitude for i in squirrel_list if i.Longitude])
    min_longitude = np.min([i.Longitude for i in squirrel_list if i.Longitude])
    running_rate = np.mean(running_rate_list)
    age_mode = max(age,key=age.get)
    age_count = age[age_mode]
    color_mode = max(fur_color,key=fur_color.get)
    color_count = fur_color[color_mode]

    context = {
            "Mean_Latitude": mean_latitude,
            "Max_Latitude": max_latitude,
            "Min_Latitude": min_latitude,
            "Mean_Longitude": mean_longitude,
            "Max_Longitude": max_longitude,
            "Min_Longitude": min_longitude,
            "Running_Rate": running_rate,
            "age_mode": age_mode,
            "age_count": age_count,
            "color_mode": color_mode,
            "color_count": color_count
    }
    return render(request, 'squirrel/stats.html',context)

