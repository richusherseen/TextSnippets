from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Snippets(models.Model):
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # tag = models.ForeignKey(Tags,on_delete=models.CASCADE)
    title = models.ForeignKey(Tags, on_delete=models.CASCADE)
    text = models.CharField(max_length=80,default='')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
