from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('home/', views.index, name="home"),
    path('menu-items/', views.MenuItemsView.as_view(), name = "menu-items"),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name = "menu-items"),
    path('user/', views.userView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]