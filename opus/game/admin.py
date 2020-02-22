from django.contrib import admin
from . import models
# Register your models here.

class AnswerAdd(admin.StackedInline):
    model=models.Story_Answer


class AptitudeAdd(admin.StackedInline):
    model=models.Aptitude_Question
    extra=3

class GameAdmin(admin.ModelAdmin):
    inlines=[AnswerAdd,AptitudeAdd]
    list_display=['question_number','question','on_good','on_medium','on_bad']
    list_display_links=['question_number']
    list_filter=['question_number']
    search_fields=['question_number']
    ordering=['question_number']




admin.site.register(models.Story_Question,GameAdmin)
admin.site.register(models.Story_Answer)
admin.site.register(models.Aptitude_Question)
admin.site.register(models.Levels)