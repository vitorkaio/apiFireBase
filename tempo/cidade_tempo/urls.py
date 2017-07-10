from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name="/"),

    # Como parte da url
    #url(r'^tempo/(?P<cidade>.+)/$', views.tempo, name="tempo"),

    # Como params request.GET['price_lte']
    url(r'^tempo/$', views.tempo, name="tempo"),
]