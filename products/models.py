from django.db import models
from shared.models import TimeStampMixin

# Create your models here.
class ProductCategory(TimeStampMixin):
   category_name = models.CharField(max_length=300)
   category_slug = models.SlugField(max_length=255, unique=True)

   def __str__(self):
        return self.category_name


class Product(TimeStampMixin):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="products"
    )
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    quantity = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    

    def __str__(self):
        return self.product_name

# class Customer(TimeStampMixin):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     address = models.TextField()

#     def __str__(self):
#         return self.name


class Order(TimeStampMixin):
    customer = models.ForeignKey(
        "accounts.Customer",
        on_delete=models.CASCADE,
        related_name="orders"
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="orders")
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.user.username}"