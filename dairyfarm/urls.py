from django.urls import path
from . import views

app_name='dairyfarm'
urlpatterns=[
	path('index', views.index, name='index'),
]