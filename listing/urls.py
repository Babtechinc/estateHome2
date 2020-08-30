from django.conf.urls import url,include
from django.urls import path
from listing import views


urlpatterns = [

path(r'',views.property,name='property'),
path(r'<int:list_item>/', views.property_full, name='property_full'),
]