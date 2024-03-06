from django.contrib import admin
from .models import *
# Register your models here.
class newUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'responseId']

class newOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'quantity', 'get_user']
    
    def get_user(self, obj):
        return obj.user.responseId
admin.site.register(new_order, newOrderAdmin)
admin.site.register(new_user, newUserAdmin)