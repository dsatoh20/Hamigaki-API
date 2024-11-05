from rest_framework import viewsets
from .models import Calender
from .serializers import CalenderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    
    # permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]