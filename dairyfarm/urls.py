from django.urls import path
from . import views

app_name='dairyfarm'
urlpatterns=[
	path('', views.index, name='index'),
]