from django.contrib import admin

# Register your models here.
from .models import profile, Contact
admin.site.register(profile)
admin.site.register(Contact)