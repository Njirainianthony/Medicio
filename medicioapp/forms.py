from django import forms
from medicioapp.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields =['name','date','doctor','email','department','message','phone']