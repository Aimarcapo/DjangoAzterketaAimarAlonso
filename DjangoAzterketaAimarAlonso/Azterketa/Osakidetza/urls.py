from . import views
from django.urls import path

urlpatterns=[
  path('Pazientea', views.pazienteak, name='paziente'),
]