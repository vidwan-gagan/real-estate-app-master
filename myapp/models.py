from django.db import models

# Create your models here.
class feature(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/',null='TRUE',blank='TRUE')
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    oname = models.CharField(max_length=500,default="NULL")
    oaddress = models.CharField(max_length=2000,default="NULL")
    omail = models.EmailField(max_length=100,default="NULL")
    ophone = models.CharField(max_length=100,default="NULL")   

class agent(models.Model):
    name = models.CharField(max_length=500)
    mail_id = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    facebook_id = models.CharField(max_length=100)
    twitter_id = models.CharField(max_length=100)
    instagram_id = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)


    