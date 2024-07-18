from django.shortcuts import render, redirect
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


