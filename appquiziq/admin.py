from django.contrib import admin


from .models import Question, Choice, Quiz
# Register your models here.
admin.site.register(Quiz)

class ChoiceInLine(admin.TabularInline):
    model = Choice
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)