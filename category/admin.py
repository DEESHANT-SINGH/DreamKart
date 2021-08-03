from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}    # as we put anything in category_name field the data will prepopulated automatically in slug field.
    list_display = ('category_name', 'slug') 

admin.site.register(Category, CategoryAdmin)