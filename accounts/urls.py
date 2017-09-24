from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),      
    url(r'^user_info/$', views.user_info, name='user_info'),    
    url(r'^password-reset-change/change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'template_name': 'accounts/password-reset-change/reset_password.html'}, name='reset-password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/password-reset-change/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/password-reset-change/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'accounts/password-reset-change/password_reset_complete.html'}, name='password_reset_complete'),
]