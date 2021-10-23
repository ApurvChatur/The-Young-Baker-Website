from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from ckeditor import fields


class Home(models.Model):
    title = models.CharField(max_length=20, unique=True, default='The Young Baker')
    subtitle = models.CharField(max_length=50, default='Your Ocassion, Our Cakes!')
    image = models.ImageField(upload_to='Home/', default='default.jpg')
    description = fields.RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:home-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:home-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:home-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:home-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:home-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True, default='Simple Cakes')
    subtitle = models.CharField(max_length=50, default='Try this simple cake... Yummy...')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # Project Model
    def get_category_url(self):
        return reverse('ProjectModel:category-page',
                       kwargs={
                           'slug': self.slug
                       })


class Product(models.Model):
    title = models.CharField(max_length=20, unique=True, default='Product Name')
    subtitle = models.CharField(max_length=50, default='Small Description')
    image = models.ImageField(upload_to='Products/', default='default.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.CharField(choices=(
                                ('featured', 'featured'),
                                ('recent', 'recent'),
                            ), max_length=20, default='featured')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:product-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:product-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:product-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:product-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:product-delete-page',
                       kwargs={
                           'slug': self.slug
                       })

    # Product Model
    def get_home_url(self):
        return reverse('ProjectModel:home-page')

    def get_products_url(self):
        return reverse('ProjectModel:products-page')

    def get_product_url(self):
        return reverse('ProjectModel:product-page',
                       kwargs={
                           'slug': self.slug
                       })

    # Project Real
    def get_real_product_url(self):
        return reverse('ProjectReal:product-page',
                       kwargs={
                           'slug': self.slug
                       })


