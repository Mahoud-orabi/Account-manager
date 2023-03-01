from django.contrib import admin
from .models import *
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("f_name",)}

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Clients,ClientAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(List)
