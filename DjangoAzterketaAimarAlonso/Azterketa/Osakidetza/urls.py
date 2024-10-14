from . import views
from django.urls import path

urlpatterns=[
  path('Pazientea/', views.pazienteak, name='paziente'),
  path('Pazientea/new', views.pazienteak_new, name='paziente-new'),
  path('Pazientea/delete/<str:variable>', views.pazienteak_delete, name='paziente-delete'),
  path('Pazientea/edit/<str:variable>', views.pazienteak_edit, name='paziente-edit'),
  path('Medikua/', views.medikuak, name='mediku'),
]