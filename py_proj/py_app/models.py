from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
status_choices = [
    ('Unpaid', 'Unpaid'),
    ('Paid', 'Paid'),
]
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    Total = models.FloatField(default=0)      #  
    Paid = models.FloatField(default=0)       # 
    Remaining = models.FloatField(default=0)  #
    status = models.CharField(max_length=100, default='Unpaid', choices=status_choices)
    paid_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.Paid > self.Remaining:
            raise ValidationError(
                f"Paid amount ({self.Paid}) cannot be greater than the remaining ({self.Remaining})"
            )
    def save(self, *args, **kwargs):
        if self.Remaining == 0:
            self.Remaining = self.Total
        self.Remaining = self.Remaining - self.Paid  #
        #self.Paid=0 
        super().save(*args, **kwargs)

    