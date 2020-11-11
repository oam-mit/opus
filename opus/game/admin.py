from django.contrib import admin
from . import models
# Register your models here.

class AnswerAdd(admin.StackedInline):
    model=models.Story_Options


class AptitudeAdd(admin.StackedInline):
    model=models.Aptitude_Question
    extra=3

class GameAdmin(admin.ModelAdmin):
    inlines=[AnswerAdd,AptitudeAdd]
    list_display=['question_number','question']
    list_display_links=['question_number']
    list_filter=['question_number']
    search_fields=['question_number','story_options__on_chosen']
    ordering=['question_number']






admin.site.register(models.Story_Question,GameAdmin)
admin.site.register(models.Story_Options)
admin.site.register(models.Aptitude_Question)
admin.site.register(models.Levels)

