from django.urls import path
from .views import UserLoginView, UserRegisterView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    # APIs to get access token and refresh token
    path('login/refreshtoken/', TokenRefreshView.as_view(),
         name='refresh-access-token'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
