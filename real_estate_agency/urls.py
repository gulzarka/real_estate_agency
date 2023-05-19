from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from property import views

urlpatterns = [
    url(r'^$', views.show_flats),
    url(r'^search/$', views.show_flats),
    url(r'^admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

