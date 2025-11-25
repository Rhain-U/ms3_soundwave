from django.contrib import admin
from .models import Event_Post, Comment, Like

# Register your models here.
admin.site.register(Event_Post)
admin.site.register(Comment)
admin.site.register(Like)
