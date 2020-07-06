from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MinLengthValidator

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField(validators=[MinValueValidator(1000)])
    description = models.TextField(default='')
    picture = models.ImageField(default='default.jpg', upload_to='uploads')
    brand = models.ForeignKey(Brand, models.SET_NULL, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_list')

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(Product, self).save(*args, **kwargs)



    