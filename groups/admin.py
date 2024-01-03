from django.contrib import admin
from .models import Group, Members

admin.site.register(Members)
admin.site.register(Group)
# Register your models here.
