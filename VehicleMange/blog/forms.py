from django import forms
from .models import Vehicle

class vehicleModelForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            'carModel',
            'location',
            'mileage',
            'NowUser'
            )

class modifyform(forms.Form):
    carModel = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    mileage = forms.IntegerField(min_value= 0)
    NowUser = forms.CharField(max_length=30)