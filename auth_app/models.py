from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class  User(AbstractUser):
  email = models.EmailField(verbose_name='email', unique=True,max_length=200)
  REQUIRED_FIELDS = ['email','first_name','last_name']
  
  USERNAME_FIELD='username'
  
  def get_username(self):
    return self.username
  