from django import forms
from medicioapp.models import Appointment,ImageModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields =['name','date','doctor','email','department','message','phone']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']

