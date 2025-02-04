from django.contrib import admin
from .models import Destination, Destination_deatils, Comments, IPAddress


# Register your models here.

admin.site.register(Destination)
admin.site.register(Destination_deatils)
admin.site.register(Comments)
admin.site.register(IPAddress)

