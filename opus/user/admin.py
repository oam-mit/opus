from django.contrib import admin
from . import models
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','user','points','reg_number','userid']
    ordering=['-points','last_answered']
    search_fields=['user__username','reg_number','userid','user__first_name','user__last_name']
    #readonly_fields=['reg_number','mob_number']
    list_per_page=20

    def name(self,obj):
        return (obj.user.first_name+' '+obj.user.last_name)

class WinnersAdmin(admin.ModelAdmin):
    readonly_fields=['user','created']
    ordering=['created']

admin.site.register(models.UserProfile,ProfileAdmin)
admin.site.register(models.Winners,WinnersAdmin)