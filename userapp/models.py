from email.policy import default
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class User(AbstractUser):
    is_super_admin= models.BooleanField('Is super admin', default=False)
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    is_user = models.BooleanField('Is user', default=True)
    phone = models.CharField(max_length=200, validators=[phone_validator], unique=True,blank=True,null=True)
    terms_and_conditions = models.BooleanField(default=True)

    

class Profile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE, max_length=1)
    image               = models.ImageField(upload_to="profilepicture", default='no_img.png')
    date_of_birthday    = models.DateField(auto_now_add=False,blank=True,null=True)
    phone               = models.CharField(max_length=15,unique=True,blank=True,null=True)
    permanent_address   = models.CharField(max_length=100,blank=True,null=True)
    present_address     = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.user.username

