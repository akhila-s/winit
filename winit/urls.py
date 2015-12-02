from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^$', 'winit.views.home', name='home'),
   url(r'^comp/$', 'winit.views.comp', name='comp'),
   url(r'^tc/$','winit.views.tc',name='tc'),
   url(r'^disc/$','winit.views.disc',name='disc'),
   url(r'^registered/$', 'winit.views.store', name='store'),
<<<<<<< HEAD
   url(r'^signin/$','winit.views.check', name='checkin'),
   url(r'^start/$','winit.views.start', name='start'),
   url(r'^start/exam/$','winit.views.exam', name='exam'),
   url(r'^thanku/$','winit.views.thanku',name='thanku'),
   url(r'^answer/$','winit.views.answer',name='answer')   
=======
<<<<<<< HEAD
   url(r'^signin/$','winit.views.check', name='checkin'),
   url(r'^start/$','winit.views.start', name='start'),
   url(r'^exam/$','winit.views.exam', name='exam'),

=======
   url(r'^signin/$','winit.views.check', name='checkin')
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
>>>>>>> cf3e7bb7c426f48ff3c6b4e61ef3aba23ab5ec56
)