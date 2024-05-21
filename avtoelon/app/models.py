from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Brend')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brandlar"

class Model(models.Model):
    name = models.CharField(max_length=255, verbose_name='Model')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    year = models.IntegerField(verbose_name='Yil')
    mileage = models.IntegerField(verbose_name='Yurgan')
    address = models.CharField(max_length=255, verbose_name='Manzil')
    price = models.IntegerField(verbose_name='Narx')
    description = models.TextField(verbose_name='Izoh')
    phone_number = models.CharField(max_length=30, verbose_name='Telefon raqam')
    pub_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='E\'lon qo\'yilgan sana')
    views = models.IntegerField(default=0, verbose_name='Ko\'rishlar soni')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brend', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Modellar"
        ordering = ['-id']

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.URLField(max_length=50, null=True, blank=True)
    instagram = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

class Comment(models.Model):
    text = models.TextField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    comentator = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Komment mualifi: {self.comentator.username}\nKomment: {self.text}'