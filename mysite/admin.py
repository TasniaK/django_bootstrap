
# Register models here to view on django admin page
# (automatic admin page that django provides)
from django.contrib import admin

from .models import Page, Section

admin.site.register(Page)
admin.site.register(Section)