from django.db import models

class Products(models.Model):

#     class Category(models.TextChoices):
#         ELECTRONICS = 'EL', 'Electronics'
#         FURNITURE = 'FU', 'Furniture'
#         CLOTHING = 'CL', 'Clothing'
#         OTHER = 'OT', 'Other'
        
        
    STATUS_CHOICES = [
        ('EL', 'Electronics'),
        ('FU', 'Furniture'),
        ('CL', 'Clothing'),
        ('OT', 'Other'),
        
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='EL')


    product_id = models.IntegerField()
    product_name = models.CharField(max_length=25)
    price = models.FloatField()
    insurance = models.BooleanField(default=False)
    mfg = models.DateField()
 
 



# from django.db import models

# # Create your models here.

# class Products(models.Model):

#     product_name = models.CharField(max_length=25)
#     price = models.IntegerField(max_length=12)
#     insurance = models.BooleanField()
#     mfg = models.DateTimeField()
    # categery = models.Choices()
    