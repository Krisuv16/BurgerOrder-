from django.db import models

# Create your models here.
class Size(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title
class Burger(models.Model):
    topping1 = models.CharField(max_length=150)
    topping2 = models.CharField(max_length=150)
    
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
