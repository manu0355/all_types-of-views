"""typesofviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from listviews.allviews.views_c import Bookview, Singlebookview, Booklistview
from listviews.allviews import views_f
from listviews.allviews.views_v import Bookviewset
from listviews.allviews.views_m import Detailsbookmixin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookall/', Bookview.as_view()),
    path('singlebook/<int:pk>/', Singlebookview.as_view()),
    path('get_book/', views_f.get_book, name = 'get_book'),
    path('create_book/', views_f.post_book, name = 'create_book'),
    path('update_book/', views_f.update_book, name = 'update_book'),
    path('bookview/', include('listviews.urls.urls_v')),
    path('mix_book/', include('listviews.urls.urls_m')),
    path('detailmix/<int:pk>/', Detailsbookmixin.as_view()),
    path('bookpage/', Booklistview.as_view()),
]
