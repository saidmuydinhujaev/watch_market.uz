
from .views import base
from django.contrib import admin
from django.urls import path, include
from .views import WatchDetailView
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductViewSet
from . import views


router = DefaultRouter()
router.register(r'watchs', ProductViewSet, basename='watchs')

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.carousel_view, name='carousel'),
    path('watch/<int:pk>/', views.WatchDetailView.as_view(), name='watch_detail'),

]

urlpatterns += router.urls