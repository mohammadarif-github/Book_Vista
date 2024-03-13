from django.contrib import admin
from .models import BookModel


class BookAdmin(admin.ModelAdmin):
    list_display = ["book_title","slug","owner","author","photo","add_date","status","pdf"]
    
    prepopulated_fields = { "slug" : ("book_title",) }
        
admin.site.register(BookModel,BookAdmin)