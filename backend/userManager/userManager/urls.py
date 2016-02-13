from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'userManager.views.home', name='home'),

    url(r'^app/', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
