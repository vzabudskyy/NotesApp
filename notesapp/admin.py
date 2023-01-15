from django.contrib import admin
from notesapp.models import Category, Notes

# Register your models here.
admin.site.register(Notes)
admin.site.register(Category)
