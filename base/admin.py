from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Message)
admin.site.register(models.Room)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Topics)
admin.site.register(models.Follows)