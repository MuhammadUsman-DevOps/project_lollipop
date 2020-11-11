from django.contrib import admin

from Lollipop_CRM.models import Customer, Sender, Package

admin.site.site_header = "Lollipop Administration"
admin.site.register(Customer)
admin.site.register(Sender)
admin.site.register(Package)
