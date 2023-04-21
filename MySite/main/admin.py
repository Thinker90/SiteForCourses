from django.contrib import admin
from .models import Post, Post_type, paid_curse

# Register your models here.

admin.site.register(Post)
admin.site.register(Post_type)
admin.site.register(paid_curse)

