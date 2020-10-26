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


admin.site.register(models.UserProfile,ProfileAdmin)
