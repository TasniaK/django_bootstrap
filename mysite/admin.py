
# Register models here to view on django admin page
# (automatic admin page that django provides)
from django.contrib import admin

from .models import Page

admin.site.register(Page)