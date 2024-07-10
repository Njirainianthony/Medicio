from django.shortcuts import render,redirect
from medicioapp.models import Contact
from medicioapp.models import Branch
from medicioapp.models import Appointment

# Create your views here.
def index(request):
    return render(request,'index.html')

def innerpage(request):
    return render(request,'inner-page.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doctors.html')

def departments(request):
    return render(request,'departments.html')

def services(request):
    return render(request,'services.html')

def contacts(request):
    if request.method == "POST":
        all=Contact(name=request.POST['name'],
                    email=request.POST['email'],
                    phone=request.POST['phone'],
                    message=request.POST['message']
                    )

        all.save()
        return redirect('/contacts')

    else:
        return render(request,'contact.html')



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


def appointment(request):
    if request.method == "POST":
        all = Appointment(name=request.POST['name'],
                        email=request.POST['email'],
                          date=request.POST['manager'],
                     department=request.POST['contact'],
                          doctor=request.POST['doctor'],
                          message=request.POST['message'],
                          phone=request.POST['phone'],

                     )

        all.save()
        return redirect('/appointment')

    else:
        return render(request, 'appointment.html')




