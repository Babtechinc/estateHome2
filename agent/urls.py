from django.conf.urls import url,include
from agent import views
from django.urls import path


urlpatterns = [

url(r'^$',views.agent_list,name='agent'),
path('<int:agent_pid>/',views.agent_full,name='agent_full')
]