from django.db import models

# Create your models here.
class Order(models.Model):
    o_id = models.IntegerField()
    name = models.CharField(max_length=60)
    organization = models.CharField(max_length=80)
    city = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, unique=True)
    last_updated_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    # active = models.BooleanField(default=True)