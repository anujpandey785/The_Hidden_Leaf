from django.contrib import admin
from social import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Friends)
admin.site.register(models.Like)
admin.site.register(models.Comment)