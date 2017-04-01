"""projectrfc URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from mainhandler import views as main_views
from opinion import views as op_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^home/", main_views.home),
    url(r"^factcheck/", op_views.fc_main),
    url(r"^register/", op_views.register),
    url(r"^submit/", op_views.save_comment),
    url(r"^comment/", op_views.res_comment),
    url(r"^vupdate/", op_views.v_update),
]
