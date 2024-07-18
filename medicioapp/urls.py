
from django.contrib import admin
from django.urls import path
from medicioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='index'),
    path('inner/', views.innerpage,name='inner'),
    path('about/', views.about,name='about'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('services/', views.services,name='services'),
    path('contacts/', views.contacts,name='contacts'),
    path('branch/', views.branch,name='branch'),
    path('appointment/', views.Appoint,name='appoint'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
]
