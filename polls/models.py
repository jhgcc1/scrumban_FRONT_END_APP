from django.db import models

from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
# Create your models here.
class uuprofile(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length=100, default='')
	country = models.CharField(max_length=100, default='')
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = uuprofile.objects.create(usuario=kwargs['instance'],email=kwargs['instance'].email)
post_save.connect(create_profile,sender=User)