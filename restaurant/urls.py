from django.urls import path
from .views import MenuListCreateView, BookingListCreateView, RegisterUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Menu API
    path('menu/', MenuListCreateView.as_view(), name='menu-list-create'),

    # Booking API
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),

    # User registration
    path('registration/', RegisterUser.as_view(), name='user-registration'),

    # JWT token auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
