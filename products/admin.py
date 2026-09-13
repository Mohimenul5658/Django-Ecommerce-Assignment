from django.contrib import admin
from .models import Product, ProductCategory, Order


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "category_slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "category",
        "price",
        "quantity",
        "is_featured",
    )

    list_filter = ("category", "is_featured")
    search_fields = ("product_name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "product",
        "quantity",
        "total_price",
        "create_at",
    )