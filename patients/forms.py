from django import forms
from .models import Details, Report


class NameForm(forms.Form):
    number = forms.CharField(label='Number', max_length=100)


class Details_Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('mobile', 'name')


class Report_Form(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('message',)
