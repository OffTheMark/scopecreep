from django.conf.urls import url, include

from . import views

app_name = 'polls'

topic_patterns = [
    url(r'^$', views.TopicView.as_view(), name='topic'),
    url(r'^edit/$', views.EditTopicView.as_view(), name='topic_edit'),
    url(r'^delete/$', views.delete_topic, name='topic_delete'),
]

suggestion_patterns = [
    url(r'^$', views.SuggestionView.as_view(), name='suggestion'),
    url(r'^vote/$', views.vote_suggestion, name='vote'),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.SigninView.as_view(), name='signin'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^topics/$', views.TopicsView.as_view(), name='topics'),
    url(r'^topic/(?P<topic_id>[0-9]+)/', include(topic_patterns)),
    url(r'^suggestion/(?P<suggestion_id>[0-9]+)/', include(suggestion_patterns)),
]
