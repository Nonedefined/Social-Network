from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Chat)
admin.site.register(MessageChat)
