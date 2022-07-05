from django.contrib import admin

from .models import Question, Choice
# Register your models here.



class ChoiceInLine(admin.TabularInline):
    model = Choice
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)