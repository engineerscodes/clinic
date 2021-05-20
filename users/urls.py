from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reg/',views.reg,name="new account"),
    path('activate/<uidb64>/<token>',views.AUTHUSERNAME,name="activate")
]
