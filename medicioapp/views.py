import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from medicioapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from medicioapp.models import Contact
from medicioapp.models import Branch
from medicioapp.models import Appointment,Product,Member,ImageModel
from medicioapp.forms import AppointmentForm,ImageUploadForm




# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']
                                 ).exists():
            members=Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request,'index.html',{'members':members})
        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')


def innerpage(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def departments(request):
    return render(request, 'departments.html')


def services(request):
    return render(request, 'services.html')


def contacts(request):
    if request.method == "POST":
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message']
                      )

        all.save()
        return redirect('/contacts')

    else:
        return render(request, 'contact.html')


def branch(request):
    if request.method == "POST":
        all = Branch(name=request.POST['name'],
                     email=request.POST['email'],

                     manager=request.POST['manager'],
                     contact=request.POST['contact'],
                     )

        all.save()
        return redirect('/branch')

    else:
        return render(request, 'branchform.html')


def Appoint(request):
    if request.method == "POST":
        appointments = Appointment(name=request.POST['name'],
                                   date=request.POST['date'],
                                   doctor=request.POST['doctor'],
                                   email=request.POST['email'],
                                   department=request.POST['department'],
                                   message=request.POST['message'],
                                   phone=request.POST['phone']
                                   )

        appointments.save()
        return redirect('/show')

    else:
        return render(request, 'appointment.html')




def show(request):
    information= Appointment.objects.all()
    return render(request,'show.html',{'data':information})


def delete(request,id):
    myappointment=Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')



def edit(request,id):
    appoint=Appointment.objects.get(id=id)
    return render(request,'edit.html',{'appointment':appoint})


def update(request,id):
    if request.method == "POST":
        appoint=Appointment.objects.get(id=id)
        form=AppointmentForm(request.POST,instance=appoint)
        if form.is_valid():
            form.save()
            return redirect('/show')

        else:
            return render(request,'edit.html')

    else:
        return render(request,'edit.html')



def register(request):
    if request.method == "POST":
        members=Member(name=request.POST['name'],
                       username=request.POST['username'],
                       password=request.POST['password'],
                       )

        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')




def login(request):
    return render(request,'login.html')






def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")


