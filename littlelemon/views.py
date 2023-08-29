from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminOrManager

'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer'''


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
    
    
    

class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=204)
    

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrManager]

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrManager]
    search_fields = ['title']
    
def home(request):
    return render(request, 'index.html')