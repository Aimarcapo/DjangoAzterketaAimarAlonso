from . import views
from django.urls import path

urlpatterns=[
  path('Pazientea/', views.pazienteak, name='paziente'),
  path('Pazientea/new', views.pazienteak_new, name='paziente-new'),
  path('Pazientea/edit/<str:variable>', views.pazienteak_edit, name='paziente-edit'),
]