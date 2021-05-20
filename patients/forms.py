from django import forms
from .models import Details, Report
import re


class NameForm(forms.Form):
    number = forms.CharField(label='Number', max_length=100)


class Details_Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('name', 'mobile',  'age', 'saturation_level', 'heart_rate', 'sex',)

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
