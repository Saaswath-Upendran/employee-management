from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    dob = models.DateField(blank=True,null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    

    def __str__(self):
        return self.user.username

    def get_absoulte_url(self):
        return reverse("employe:detail",kwargs={'pk':self.pk})



class EmployeeWorkingHours(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True,null=True)
    end_time = models.DateTimeField(blank=True,null=True)

    



