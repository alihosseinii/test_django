from django.db import models
from user.models import UserInformation
from train.models import ExistTrains

class Reservation(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    train = models.ForeignKey(ExistTrains, on_delete=models.CASCADE)
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

        