from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^$', 'winit.views.home', name='home'),
   url(r'^registered/$', 'winit.views.store', name='store'),
<<<<<<< HEAD
   url(r'^signin/$','winit.views.check', name='checkin'),
   url(r'^start/$','winit.views.start', name='start'),
   url(r'^exam/$','winit.views.exam', name='exam'),

=======
   url(r'^signin/$','winit.views.check', name='checkin')
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
)