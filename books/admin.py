from django.contrib import admin

from .models import Book
# Register your models here.

# admin.site.register(Book)  # this registration is also OK, but it is less informative

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "subtitle", "author")
    list_display_links = ("id", "author")
    search_fields = ("title", "author")