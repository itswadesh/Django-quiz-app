from django.contrib import admin
from .models import Category, Question, Answers


# Register your models here.


admin.site.register(Category)

class AnswersAdmin(admin.StackedInline):
    model = Answers


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersAdmin]



admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers)