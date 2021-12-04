from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile
import uuid

# Create your models here.

class Item(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    item_pic = models.ImageField(upload_to ='item_pic')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    digital = models.BooleanField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
