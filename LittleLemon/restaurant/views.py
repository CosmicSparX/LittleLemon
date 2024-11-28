from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


def index(request):
    return render(request, 'index.html', {})

