from django.contrib import admin
from users.models import Snippets, Tags

admin.site.register(Tags)
admin.site.register(Snippets)