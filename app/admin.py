from django.contrib import admin
from .models import Vehicle, ServiceRecord, Position, Staff

# admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(ServiceRecord)
admin.site.register(Position)
admin.site.register(Staff)