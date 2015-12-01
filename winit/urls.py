from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^$', 'winit.views.home', name='home'),
   url(r'^registered/$', 'winit.views.store', name='store'),
   url(r'^signin/$','winit.views.check', name='checkin'),
   url(r'^start/$','winit.views.start', name='start'),
   url(r'^exam/$','winit.views.exam', name='exam'),

)