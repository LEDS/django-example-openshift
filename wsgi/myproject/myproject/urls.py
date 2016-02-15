from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'polls.views.home', name='home'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
