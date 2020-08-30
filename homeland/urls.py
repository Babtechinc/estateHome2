from django.conf.urls import url
from django.urls import path
from homeland import views

urlpatterns = [
    url(r'^$',views.try1,name='try1'),
    path('login/',views.loginPage, name='login'),
     path('register/',views.registerPage, name='register'),
]