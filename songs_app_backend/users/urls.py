from django.urls import path
from .views import UserLoginView, UserRegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    # APIs to refresh token
    path('login/refreshtoken/', TokenRefreshView.as_view(),
         name='refresh-access-token'),
]
