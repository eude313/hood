from django.contrib import admin
from .models import *
# Register your models here.

models=[Users, Post, Hood,Business,Health,Police]

# Register your models here.
for model in models:
    admin.site.register(model)


admin.site.site_header = "Hood Admin"
admin.site.site_title = "Hood Admin Portal"
admin.site.index_title = "Hood Portal"