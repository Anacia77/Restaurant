from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('api-token-auth', obtain_auth_token),

    #path('restaurant/', include(router.urls)),
    #path('restaurant/booking/', include(router.urls), name='booking'),
    
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('', views.home, name='home'),

    path('booking', views.BookingView.as_view(), name='booking'),
    path('menu-items', views.MenuView.as_view(), name= 'menu'),
    path('menu-items/<int:pk>', views.SingleMenuView.as_view()),
]