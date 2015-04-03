from django.contrib import admin
from .models import Post,Comment,bloguser
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(bloguser)
# Register your models here.
