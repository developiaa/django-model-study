from django.contrib import admin

# Register your models here.
from model.post import Post
from model.comment import Comment

admin.site.register(Post)
admin.site.register(Comment)
