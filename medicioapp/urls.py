
from django.contrib import admin
from django.urls import path
from medicioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('inner/', views.innerpage,name='inner'),
    path('about/', views.about,name='about'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('services/', views.services,name='services'),
    path('contacts/', views.contacts,name='contacts'),
    path('branch/', views.branch,name='branch'),
    path('appointment/', views.appointment,name='branch'),
]
