from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^demo/', views.demo, name='demo'),
    url(r'^medium/', views.medium, name='medium'),
    url(r'^gent/', views.gent, name='gent'),
    url(r'^cmu/', views.cmu, name='cmu'),
    url(r'^d3/', views.d3, name='d3'),
    url(r'^ieee123/', views.ieee123, name='ieee123'),
]
