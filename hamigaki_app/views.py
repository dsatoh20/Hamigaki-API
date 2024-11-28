from rest_framework import viewsets
from .models import Calender, Notification
from .serializers import CalenderSerializer, NotificationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    permission_classes = [AllowAny]