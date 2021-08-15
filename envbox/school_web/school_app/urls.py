#Url of app
from school_app import views
from django.urls import path
from school_app.views import *

urlpatterns = [
    path('',views.homepage,name='home'),
    path('register/',views.register,name='register'),
    path('loginin/',views.login_backend,name='login_user'),
]