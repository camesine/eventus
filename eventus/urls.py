from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('app.events.urls', namespace="events_app")),
    url(r'^admin/', admin.site.urls),
]
