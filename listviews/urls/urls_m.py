from django.urls import include, path
from django.conf. urls import url
# from rest_framework.routers import DefaultRouter
from listviews.allviews.views_m import Listbookmixin, Detailsbookmixin

# router = DefaultRouter()
# router.register('mixinbook', Listbookmixin, basename= 'mixinbook')

urlpatterns = [
    path('mixbook/', Listbookmixin.as_view()),
    # path('deatilsmixin/<int:pk>/', Detailsbookmixin.as_view()),
    
]