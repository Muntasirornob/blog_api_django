from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Post(models.Model):
  title=models.CharField(max_length=100)
  content=models.TextField()
  author=models.ForeignKey(User,on_delete=models.CASCADE)
    
  def __str__(self):
  	return self.title


class Profile (models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.png',upload_to='profile_pics')


	def  __str__(self):
		return f'{self.user.username} profile'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)