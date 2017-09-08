from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'app.events.views.index', name="index"),
    url(r'^panel/$', 'app.events.views.main_panel', name="panel"),
    url(r'^panel/evento/nuevo/$', 'app.events.views.crear_evento', name="nuevo"),   
)
