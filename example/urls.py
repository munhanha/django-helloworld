from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'simpleHW/', views.helloWorld),
    url(r'simpleHWTemplate/', views.helloWorldTemplate),
    url(r'simpleHWJSON/', views.helloWorldJSON),
]