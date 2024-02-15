from django.db import models


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'ID: {self.id} {self.name}'


class Product(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    price = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'ID: {self.id} {self.name}'




