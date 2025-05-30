from django.contrib import admin
from .models import Product, Brand, Category


admin.site.site_header = "Администрирование КФ Виктории"
admin.site.site_title = "Админ-панель"
admin.site.index_title = "Админ-панель КФ Виктории"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category")
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass