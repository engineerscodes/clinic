from django.urls import path
from . import views

app_name = "patients"
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('view/', views.view, name='view'),
    path('view/<int:number>/', views.display, name='display'),
    path('report/', views.report, name='report'),
    path('info/', views.index, name='index')
]
