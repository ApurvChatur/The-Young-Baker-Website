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


class Product(models.Model):
    title = models.CharField(max_length=20, unique=True, default='Product Name')
    subtitle = models.CharField(max_length=50, default='Small Description')
    image = models.ImageField(upload_to='Products/', default='default.jpg')
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


