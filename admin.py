from django.contrib import admin
from django.contrib.auth.models import Group as OldGroup
from .models import User, Group

# Register your models here.
admin.site.unregister(OldGroup)
admin.site.register(User)
admin.site.register(Group)

