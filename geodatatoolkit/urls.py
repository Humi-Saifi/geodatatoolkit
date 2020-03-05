"""geodatatoolkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('sensors/cloud',views.sensorDataCloud),
    path('sensors/local',views.sensorDataLocal),
    path('api/sensor/1',views.ApiSensor1),
    path('api/sensor/2',views.ApiSensor2),
    path('api/sensor/3',views.ApiSensor3),
    path('api/sensor/4',views.ApiSensor4),
    path('api/remote/sensor/1',views.ApiRemoteSensor1),
    path('api/remote/sensor/2',views.ApiRemoteSensor2),
    path('api/remote/sensor/3',views.ApiRemoteSensor3),
    path('api/remote/sensor/4',views.ApiRemoteSensor4),
    path('api/local/sensor/1',views.ApiLocalSensor1),
    path('api/local/sensor/2',views.ApiLocalSensor2),
    path('api/local/sensor/3',views.ApiLocalSensor3),
    path('api/local/sensor/4',views.ApiLocalSensor4),
    path('api/com/port',views.runComPort),
    path('api/deconnect',views.deconnect),
    path('dashboard',views.dashboard),

]
