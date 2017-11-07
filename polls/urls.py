from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
]
