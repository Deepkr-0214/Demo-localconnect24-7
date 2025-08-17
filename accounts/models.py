from django.db import models
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    delivery_address = models.TextField(null=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customers'

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if not self.pk:  # Only hash on creation
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email})"
