from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.SigninView.as_view(), name='signin'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^topics/$', views.TopicsView.as_view(), name='topics'),
    url(r'^topic/(?P<pk>[0-9]+)/$', views.TopicView.as_view(), name='topic'),
    url(r'^topic/(?P<pk>[0-9]+)/edit/$', views.EditTopicView.as_view(), name='topic_edit'),
    url(r'^topic/(?P<topic_id>[0-9]+)/delete/$', views.delete_topic, name='topic_delete'),
    url(r'^suggestion/(?P<pk>[0-9]+)/$', views.SuggestionView.as_view(), name='suggestion'),
]
