from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Catalog(CMSPlugin):
    alternate = models.BooleanField(default=False)

class Detail(CMSPlugin):
    test = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=50, default=None, null=True)
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True)
    description = models.TextField(max_length=20000, default='Product description...', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to='addyart/static/products/', null=True )

    def __str__(self):
        return self.name
