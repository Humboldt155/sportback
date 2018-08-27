from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SportRudView

app_name='sports'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', SportRudView.as_view(), name='sport-rud'),
    # url(r'^sports/(?P<pk>[0-9]+)/$', views.SportList.as_view(), name='sport-detail'),
]
