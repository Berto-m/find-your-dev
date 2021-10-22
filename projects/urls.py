from django.urls import path
from . import views

#from . import views. imports everything from views
urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
]