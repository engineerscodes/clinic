from django.contrib import admin
from .models import DOCTORS
from django.contrib.auth.models import User
# Register your models here.



class DOCADMIN(admin.ModelAdmin):
    model = DOCTORS
    list_filter  = ('doctor',)
    search_fields=('doctor',)



admin.site.register(DOCTORS,DOCADMIN)