
from django.contrib import admin
from info.models import Hashtags, Publications, Category, Contacts

@admin.register(Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
   list_display = ['name']
