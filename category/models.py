from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)    # blank = True  means it is optional
    cat_image = models.ImageField(upload_to='photos/catogories/', blank=True)   #upload_to = when we upload a file where should it go (path)

    class Meta:         # If we not include this then django will take plural form of category as categorys in admin panel. which is not good a typo
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
