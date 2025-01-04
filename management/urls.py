from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    LoginView,
    LogoutView,
    UserDetailEditView,
    UserDetailView,
    CompanyDetailView,
    CompanyViewSet,
    CustomUserViewSet,
)

router = DefaultRouter()
router.register("companies", CompanyViewSet)
router.register("users", CustomUserViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/detail/", UserDetailView.as_view(), name="user_detail"),
    path("user/edit/", UserDetailEditView.as_view(), name="user_detail_edit"),
    path(
        "company/<int:company_id>/", CompanyDetailView.as_view(), name="company_detail"
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
]
