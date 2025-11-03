from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInformation(AbstractUser):
    phone_number  = models.CharField(max_length=20, unique=True)
    name = models.CharField(blank=True, null=True)
    nationality = models.CharField(blank=True, null=True)
    national_code = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length= 1,
        choices=[
            ('M','Male'),
            ('F','Female'),
        ],
        blank=True, null=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    home_number = models.BigIntegerField(blank=True, null=True)
    essential_number = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"user with number -> {self.phone_number}"

    class Meta:
        db_table = "userinformation"


