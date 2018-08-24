


from django.conf.urls import url, include
from django.contrib import admin
from App1 import views


# Template Tagging

app_name = 'App1'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('register/$', views.register, name='register'),
    url('user_login/$', views.user_login,name='user_login'),
]
