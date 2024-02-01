from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=3000, default='')
    price = models.IntegerField(null=False, default=0)
    amount = models.IntegerField(null=False, default=0)

    class Meta:
        verbose_name = 'Product'  # Category
        verbose_name_plural = 'Products'  # Categories

    def __str__(self):
        return f'ID: {self.id} {self.name}'


# Category - Categories Error: Categorys

