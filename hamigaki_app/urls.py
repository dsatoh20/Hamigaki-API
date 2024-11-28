from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'calenders', views.CalenderViewSet)
router.register(r'notifications', views.NotificationViewSet)

urlpatterns = [
    path('', include(router.urls))
]