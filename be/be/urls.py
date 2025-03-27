from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, CustomTokenObtainPairView,UserProfileView  # Import custom view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register", CreateUserView.as_view(), name="register"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="get_token"),  # Use custom view
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
     path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]