from django.contrib import admin
from .models import Details, Report


class patientsinfoAdmin(admin.ModelAdmin):
    list_filter = ('mobile','Form_date','name')
    list_display = ('mobile', 'name','is_checked',)
    search_fields = ('mobile', 'name')
    readonly_fields=('name','is_checked','Form_date')

class REPORT_ADMIN(admin.ModelAdmin):
    list_filter = ('patient', 'doctor_name')
    list_display =  ('patient', 'doctor_name','client_name')
    search_fields =  ('patient', 'doctor_name')
    readonly_fields = ( 'doctor_name','client_name')

admin.site.register(Details, patientsinfoAdmin)
admin.site.register(Report,REPORT_ADMIN)
