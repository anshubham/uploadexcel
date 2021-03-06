"""CATS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
# from django.conf.urls.defaults import *	
from django.contrib import admin
from django.conf import settings
from fileupload import views

admin.autodiscover()
urlpatterns = [
	url(r'^fileupload/', include('fileupload.urls')),
    url(r'^admin/', admin.site.urls),
    
]




# from django.conf.urls import include, patterns, url 

if settings.DEBUG: 
	import debug_toolbar 
	urlpatterns += patterns('' ,
		url(r'^__debug__/', include(debug_toolbar.urls)), 
)

