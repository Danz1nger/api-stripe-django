from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import BuyItemView, ItemView, MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', obtain_auth_token),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('api/items/<int:id>/buy/', BuyItemView.as_view(), name='buy_item'),
    path('api/items/<int:id>/', ItemView.as_view(), name='item_detail'),
    path('api/', include('api_stripe.urls')),
]