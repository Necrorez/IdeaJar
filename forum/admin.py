from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title','auther','slug',)
    prepopulated_fields = {'slug':('title',),}

admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Reply)