from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .views import RegisterAPIView, UserViewSet

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', RegisterAPIView.as_view())
]

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')


urlpatterns += router.urls
