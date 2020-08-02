from django.contrib import admin

from .models import *

admin.site.site_header = "Vet Report Administration"
admin.site.site_title = "Vet Report Admin Room"
admin.site.index_title = "Vet Report | Admin Room"

admin.site.register(Client)
admin.site.register(Case)
