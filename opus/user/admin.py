from django.contrib import admin
from . import models
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','user','points']
    ordering=['-points']
    search_fields=['user','name']
    #readonly_fields=['reg_number','mob_number']

    def name(self,obj):
        return (obj.user.first_name+' '+obj.user.last_name)

class WinnersAdmin(admin.ModelAdmin):
    readonly_fields=['user','created']
    ordering=['created']

admin.site.register(models.UserProfile,ProfileAdmin)
admin.site.register(models.Winners,WinnersAdmin)