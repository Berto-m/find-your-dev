from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #include grabs all the urls from projects.url
    path('', include('projects.urls')),
]