from . import views
from django.urls import path

urlpatterns=[
  path('', views.zitak, name='index'),
  path('Zita/berria', views.zitak_new, name='zita-new'),
  path('Zita/edit/<int:id>', views.zitak_edit, name='zita-edit'),
  path('Zita/delete/<int:id>', views.zita_delete, name='zita-delete'),
  path('Pazientea/', views.pazienteak, name='paziente'),
  path('Pazientea/new', views.pazienteak_new, name='paziente-new'),
  path('Pazientea/delete/<str:variable>', views.pazienteak_delete, name='paziente-delete'),
  path('Pazientea/edit/<str:variable>', views.pazienteak_edit, name='paziente-edit'),
  path('Medikua/', views.medikuak, name='mediku'),
  path('Medikua/new', views.medikuak_new, name='mediku-new'),
  path('Medikua/delete/<int:variable>', views.medikuak_delete, name='mediku-delete'),
  path('Medikua/edit/<int:variable>', views.medikuak_edit, name='mediku-edit'),
]