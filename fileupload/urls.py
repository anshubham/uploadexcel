from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'processfile/$', views.process_file, name='processfile' ),
]