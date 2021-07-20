from django.db import models

class user_Table(models.Model):
     name = models.CharField(max_length=10)
     email= models.EmailField()
     txt = models.CharField(max_length=500)

