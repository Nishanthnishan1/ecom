from django.contrib import admin
from . models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catadmin)


class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','stock','img','price']
    list_editable=['stock','img','price']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,prodAdmin)

admin.site.register(UserProfile)
admin.site.register(Login)
