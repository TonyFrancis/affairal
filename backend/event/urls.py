from django.conf.urls import url, include
from .views import ListEvent

urlpatterns = [
    url(r'^$',ListEvent.as_view(), name='index'),
]
