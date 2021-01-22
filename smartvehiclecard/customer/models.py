from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    confirmpw = models.CharField(max_length=100,default=())


    class Meta:
        db_table = "customer"
