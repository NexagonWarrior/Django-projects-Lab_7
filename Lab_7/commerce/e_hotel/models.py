from django.db import models

class Hotel(models.Model):
    name        = models.CharField(max_length=120)
    city        = models.CharField(max_length=80)
    price       = models.PositiveIntegerField()   # $ за ніч
    rooms_free  = models.PositiveIntegerField()   # скільки вільних
    image       = models.ImageField(upload_to='hotel/')
    def __str__(self): return f"{self.name} — {self.city}"
