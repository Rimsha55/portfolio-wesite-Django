from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    head0 = models.CharField(max_length=500,default='')
    head1 = models.CharField(max_length=500,default='')
    head2 = models.CharField(max_length=500,default='')
    # mny imaage my upload to esliyn kiya h tkn  image a path cleraly define hu media m blog phir img
    thumbnail = models.ImageField(upload_to='blog/image',default='')
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title