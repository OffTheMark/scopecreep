from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.SigninView.as_view(), name='signin'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
]
