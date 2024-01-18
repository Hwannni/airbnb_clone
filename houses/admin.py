from django.contrib import admin
from .models import House
# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    fields = ("name", "address", ("price", "pets_allowed")) 
    list_display = ("name", "price", "address", "pets_allowed")
    list_filter = ("price", "pets_allowed")
    search_fields = ("address",) # one-item tuple 이라면 , 필수
    list_display_links = ("name", "address")
    list_editable = ("pets_allowed", )