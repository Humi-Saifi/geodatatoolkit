from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from collections import namedtuple

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    return render(request,"index.html",{})

def sensorData(request):
    return render(request,"sensors.html",{})

def ApiSensor1(request):
    all_data=None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM disto")
        all_data=dictfetchall(cursor)
    print(all_data)
    #return render(request,"sensors.html",{})
    return JsonResponse(all_data,safe=False)

def ApiSensor2(request):
    all_data=None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM gpsnn")
        all_data=dictfetchall(cursor)
    print(all_data)
    #return render(request,"sensors.html",{})
    return JsonResponse(all_data,safe=False)  

def ApiSensor3(request):
    all_data=None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sensordata")
        all_data=dictfetchall(cursor)
    print(all_data)
    #return render(request,"sensors.html",{})
    return JsonResponse(all_data,safe=False)     
