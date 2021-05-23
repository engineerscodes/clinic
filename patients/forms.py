from django import forms
from .models import Details, Report
import re


class NameForm(forms.Form):
    number = forms.CharField(
        label='Number', max_length=10, min_length=10)

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['placeholder'] = 'Enter your mobile number'

    def clean(self):
        super(NameForm, self).clean()
        number = self.cleaned_data.get('number')

        if len(number) < 10:
            self._errors['name'] = self.error_class([
                'Name should not be less than 10 characters'])
        if len(number) > 10:
            self._errors['name'] = self.error_class([
                'Name should not be less than 10 characters'])
        if not str(number).isdecimal():
            self._errors['mobile'] = self.error_class([
                'Enter only numbers'])


class Details_Form(forms.ModelForm):

    class Meta:
        model = Details
        fields = ('name', 'mobile', 'age', 'saturation_level', 'heart_rate', 'sex', 'symptoms')

    def __init__(self, *args, **kwargs):
        super(Details_Form, self).__init__(*args, **kwargs)
        self.fields['mobile'].widget.attrs['placeholder'] = 'Enter your mobile number'
        self.fields['name'].widget.attrs['placeholder'] = "Enter your name"
        self.fields['symptoms'].widget.attrs['placeholder'] = "Enter your symptoms"

    def clean(self):
        super(Details_Form, self).clean()
        name = self.cleaned_data.get('name')
        mobile = self.cleaned_data.get('mobile')
        age = self.cleaned_data.get('age')

        if len(name) < 5:
            self._errors['name'] = self.error_class([
                'Name should not be less than 5 characters'])

        if not bool(re.match('[a-zA-Z\s]+$', name)):
            self._errors['name'] = self.error_class([
                'Enter a valid name'])

        if len(mobile) < 10 or len(mobile) > 10:
            self._errors['mobile'] = self.error_class([
                'Enter valid 10 digit mobile number'])

        if not str(age).isdecimal():
            self._errors['age'] = self.error_class([
                'Enter valid age'])

        if not str(mobile).isdecimal():
            self._errors['mobile'] = self.error_class([
                'Enter only numbers'])

        return self.cleaned_data


class Report_Form(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('message',)

    def __init__(self, *args, **kwargs):
        super(Report_Form, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['placeholder'] = 'Enter message'
