

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


from django.contrib import admin
from django.urls import path
from Informationapp import views
app_name = 'Informationapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('', views.Home, name='Home'),

]
