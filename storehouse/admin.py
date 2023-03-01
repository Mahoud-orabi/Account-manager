from django.contrib import admin
from .models import Store,Category
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}



admin.site.register(Store,StoreAdmin)
admin.site.register(Category)