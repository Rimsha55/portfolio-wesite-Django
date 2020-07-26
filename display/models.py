from django.db import models

# Create your models here.

class profile(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length= 200)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name