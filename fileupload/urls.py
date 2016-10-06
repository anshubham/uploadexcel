from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'file/$', views.upload_file, name='fileupload' ),
    url(r'printsome/$', views.printsome, name='printsome' ),

]