from django.db import models
from accounts.models import CustomUser, City


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    quantity = models.PositiveIntegerField(verbose_name="وزن هر بسته (کیلو گرم)")

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام انبار")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="شهر")

    def __str__(self):
        return f'{self.name} {self.city.name}'


class InventoryStock(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="نام محصول")
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name="نام انبار")
    stock = models.PositiveIntegerField(blank=False, verbose_name="موجودی")

    def __str__(self):
        return self.name.name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="مشتری")
    product = models.ForeignKey(InventoryStock, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="تعداد")

    PROGRESSING = 'در حال بررسی'
    CONFIRMED = 'تایید شده'
    DENIED = 'عدم تایید'
    STATUS_CHOICES = [
        (PROGRESSING, 'در حال بررسی'),
        (CONFIRMED, 'تایید شده'),
        (DENIED, 'عدم تایید'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PROGRESSING, verbose_name="وضعیت")

    def __str__(self):
        return f'{self.user.username} -> {self.product} * {self.quantity}'
