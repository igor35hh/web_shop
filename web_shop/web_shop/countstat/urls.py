from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^countstat/(?P<category_id>\d+)/$', views.ReadStat, name='ReadStat'),
    url(r'^countstat/all/$', views.ReadStatAll, name='ReadStatAll')
]
