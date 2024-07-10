from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.CharField(max_length=200)
    color=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name



class Branch(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    manager=models.CharField(max_length=200)
    email=models.EmailField()
    contact=models.IntegerField()
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    doctor=models.CharField(max_length=200)
    email=models.EmailField()
    department=models.CharField(max_length=200)
    message=models.TextField()
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name


