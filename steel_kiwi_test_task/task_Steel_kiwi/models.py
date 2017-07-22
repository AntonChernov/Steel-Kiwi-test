from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=300, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

    def as_dict(self):
        items = {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
        }
        return items


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(max_length=400, null=True)
    price = models.FloatField(default=float(0.00))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

    def as_dict(self):
        items = {
            'id': self.id,
            'category': self.category.name,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'price': self. price,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
        }
        return items

















