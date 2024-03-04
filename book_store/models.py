from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_author = models.BooleanField(default=False)

    
class BookModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    book_title = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(null=False,unique=True)
    author = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    add_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='book_photos/',blank=True,null=True)
    def __str__(self):
        return self.book_title
    