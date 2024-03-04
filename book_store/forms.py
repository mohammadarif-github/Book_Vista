from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BookModel
from django import forms
from django.utils.text import slugify


class RegistrationForm(UserCreationForm):
    class Meta :
        model = User
        fields = [ "username", "first_name" ,'email' , 'password1' ,'password2' ]
        
class AddBookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ["book_title","author","description","photo"]
        labels = {
            "book_title" : "Book Title",
            "author" : "Author Name",
            "description" : "Description",
            "photo" : "Image"
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.book_title)
        if commit:
            instance.save()
        return instance
        