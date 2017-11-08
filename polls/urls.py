from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.SigninView.as_view(), name='signin'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^topics/$', views.TopicsView.as_view(), name='topics'),
]
