from rest_framework import serializers
from .models import Calender, Notification
from datetime import timedelta


class CalenderSerializer(serializers.ModelSerializer):
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Calender
        fields = '__all__'
        

    def get_end_date(self, obj):
        return obj.start_date + timedelta(days=obj.duration-1)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'