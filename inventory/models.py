from django.db import models

# Create your models here.

class InventoryModel(models.Model):
    Name = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=1000)
    Description = models.CharField(max_length=1000)
    InvoiceNo = models.CharField(max_length=1000)
    Warranty = models.CharField(max_length=1000)
    Price = models.CharField(max_length=1000)
    Department = models.CharField(max_length=1000)
    PurchasingDate = models.CharField(max_length=1000)
    # Image = models.ImageField()

    def __str__(self):
        return self.Name
