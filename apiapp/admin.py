from django.contrib import admin
from .models import Work,Featured,GearCategory,GearItem

# Register your models here.
admin.site.register(Work)
admin.site.register(Featured)
admin.site.register(GearCategory)
admin.site.register(GearItem)