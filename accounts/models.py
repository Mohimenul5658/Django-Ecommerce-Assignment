from django.db import models
from django.contrib.auth.models import User
from shared.models import TimeStampMixin

# Create your models here.
class Address(TimeStampMixin):
   country = models.CharField(max_length=255)
   city = models.CharField(max_length=255)
   postal_code = models.CharField(max_length=10)
   address_line = models.CharField(max_length=550)

   def __str__(self):
      return f"{self.address_line}-{self.city}-{self.country}"


class customer(TimeStampMixin):
   user =  models.OneToOneField(to=User,on_delete=models.CASCADE, related_name='customer')
   phone = models.CharField(max_length=15)
   profile_image= models.ImageField(upload_to='profile')
   address = models.ManyToManyField(to=Address, related_name='address')

   def __str__(self):
         return f"{self.user.username}"
