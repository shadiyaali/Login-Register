from django.db import models

# Create your models here.

class userdata(models.Model):
    user_name =models.CharField(max_length=100)
    user_password =models.CharField(max_length=100)


