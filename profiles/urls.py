from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('', url(r'^$', views.home, name='profile-index'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'profiles/login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^edit/$', views.update_user),
                       url(r'^create/$', views.create_user),
                       )
