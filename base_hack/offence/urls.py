from django.conf.urls import include, url
from offence import views

urlpatterns = [
    url(r'^batters/', views.batters),
]
