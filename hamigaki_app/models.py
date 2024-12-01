from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from account.models import User


class Calender(models.Model):
    title = models.CharField(max_length=16) # title
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calender_owner')
    purpose = models.TextField(null=True, blank=True) # 意気込み
    start_date = models.DateTimeField(default=timezone.now) # 開始日
    duration = models.IntegerField(default=31, validators=[MinValueValidator(7), MaxValueValidator(365)]) # 1週間~1年
    status = models.JSONField(default=[0]) # 進捗状況
    completed = models.BooleanField(default=False) # Completed?
    public = models.BooleanField(default=False) # Groupに公開するかどうか
    
    def save(self, *args, **kwargs):
        if self.status == [0]:
            self.status = [0] * self.duration
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f'Calender:id={self.id}, {self.title}({self.owner})'

class Notification(models.Model):
    title = models.CharField(max_length=16)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_owner')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_reciever')
    read = models.BooleanField(default=False) # 既読チェック
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Notification:id={self.id}, {self.title} from {self.owner} to {self.reciever}'