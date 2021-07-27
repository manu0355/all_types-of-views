from django import urls
from django.urls import path, include
from django.conf.urls import url
from listviews.allviews.views_v import Bookviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bookviewset', Bookviewset, basename='bookviewset')

urlpatterns = [
    url('', include(router.urls))
]