from django.db import models

# Create your models here.

class Product_category(models.Model):
    pc_id=models.PositiveIntegerField()
    pc_name=models.CharField(max_length=100)


    def __str__(self):
        return self.pc_name
    
class Product(models.Model):
    pc_name=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    p_id=models.PositiveIntegerField()
    p_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    desc=models.TextField()


    def __str__(self):
        return self.p_name
