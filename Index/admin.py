from django.contrib import admin
from . import models
# Register your models here.
class ChangeAdmin(admin.ModelAdmin):
    list_display = ["name" , "email" , "date" , "readed_by_admin"]
    list_filter = ["date" , "readed_by_admin"]
admin.site.register(models.Contact_Us_db , ChangeAdmin)
admin.site.register(models.Producdt )
admin.site.register(models.Tag )
admin.site.register(models.NewsUser )