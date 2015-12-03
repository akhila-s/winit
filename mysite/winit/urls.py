from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^$', 'winit.views.home', name='home'),
   url(r'^comp/$', 'winit.views.comp', name='comp'),
   url(r'^tc/$','winit.views.tc',name='tc'),
   url(r'^disc/$','winit.views.disc',name='disc'),
   url(r'^registered/$', 'winit.views.store', name='store'),
   url(r'^signin/$','winit.views.check', name='checkin'),
   url(r'^start/$','winit.views.start', name='start'),
   url(r'^start/exam/$','winit.views.exam', name='exam'),
   url(r'^thanku/$','winit.views.thanku',name='thanku'),
   url(r'^answer/$','winit.views.answer',name='answer')   
)