from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, login_user, logout_user, current_user, get_csrf_token

router = DefaultRouter()
router.register(r'account', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('current-user/', current_user, name='current_user'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_tokne'),
]
