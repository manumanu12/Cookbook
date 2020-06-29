from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class TelegramProfile(models.Model):
    name = models.CharField(default="",max_length=200,blank=True,unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_id")
    telegram_chat_id = models.CharField(max_length=40,default="",editable=True,blank=True,unique=True)

    def __str__(self):
        return str(self.name)

# @receiver(post_save, sender=User)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         TelegramProfile.objects.create(user=instance)
#
# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,**kwargs):
#     instance.profile.save()