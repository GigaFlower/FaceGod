"""FaceGod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from main import views

urlpatterns = [
    url(r'^upload$', views.upload),
    url(r'^upload/photo/(.+)', views.upload_photo),
    url(r'^get/photo/(.+)', views.get_photo),
    url(r'^delete/([0-9]+)', views.delete),
    url(r'^delete$', views.delete_all),

    url(r'^get/ranking$', views.get_ranking),
    url(r'^get/detail$', views.get_detail),

    url(r'^upload/statistic', views.upload_sta),
    url(r'^get/statistic', views.get_sta),
    url(r'^delete/statistic', views.delete_sta),

    url(r'^match/([0-9]+)/(.+)', views.set_match),
    url(r'^unmatch/([0-9]+)', views.unset_match),

    url(r'^admin/', admin.site.urls),
    url(r'', views.hello)
]
