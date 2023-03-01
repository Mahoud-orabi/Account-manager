from django.contrib import admin
from .models import * 
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("f_name",)}

admin.site.register(Person,PersonAdmin)
admin.site.register(Day)