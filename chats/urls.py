from django.conf.urls import url
from . import views
from accounts import views as accounts_views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', accounts_views.home),
    url(r'^create_chat/$', views.create_chat, name='create-chat'),
    url(r'^join_chat/$', views.join_chat, name='join-chat'),
    url(r'^chat?/$', views.entered_chat, name='entered-chat'),
    url(r'^get_my_user_info/$', views.get_my_user_info, name='my-user')
]