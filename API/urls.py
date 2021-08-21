from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'authors', views.AuthorViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('api-path',include('rest_framework.urls',namespace='rest_framework')),
]