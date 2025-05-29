from django.contrib import admin
from .models import Instrument

admin.site.site_header = "Smart Traffic Control Panel"
admin.site.site_title = "Smart Traffic Admin"
admin.site.index_title = "Welcome to the Traffic Signal Dashboard"

admin.site.register(Instrument)
