from django.shortcuts import render,redirect
from medicioapp.models import Contact

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



