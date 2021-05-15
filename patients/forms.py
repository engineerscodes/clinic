from django import forms
from .models import Details


class Details_Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('mobile', 'name')
