from django.db import models
from user.models import UserInformation
from train.models import Train
from django.core.exceptions import ValidationError

class Reservation(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveBigIntegerField(editable=False)  
    reserved_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.train and hasattr(self.train, 'price'):
            self.total_price = self.train.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} → {self.train} × {self.quantity}"
    
    class Meta:
        db_table = 'reservation'


class Passenger(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='passengers', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    national_id = models.CharField(max_length=10) 

    def clean(self):
        if not self.national_id.isdigit() or len(self.national_id) not in (10, 11):
            raise ValidationError({'national_id': 'کدملی باید عددی و طول درست داشته باشد.'})

    def str(self):
        return f"{self.full_name} ({self.national_id})"