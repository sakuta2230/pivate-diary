from django.contrib import admin
from .models import blog
from .models import blogcon
from django.contrib.auth import get_user_model

customuser = get_user_model()

admin.site.register(customuser)
from django.contrib.auth import get_user_model

admin.site.register(blog),
admin.site.register(blogcon)

