from django.contrib import admin
from .models import *


class AreasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Areas._meta.fields]

    class Meta:
        model = Areas


admin.site.register(Areas, AreasAdmin)


class AnswerLevel1Admin(admin.TabularInline):
    model = AnswerLevel1


class CheckQuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CheckQuestion._meta.fields]

    class Meta:
        model = CheckQuestion


admin.site.register(CheckQuestion, CheckQuestionAdmin)


class QuestionLevel1Admin(admin.ModelAdmin):
    list_display = [field.name for field in QuestionLevel1._meta.fields]
    inlines = [AnswerLevel1Admin]

    class Meta:
        model = QuestionLevel1


admin.site.register(QuestionLevel1, QuestionLevel1Admin)


class QuestionLevel2Admin(admin.ModelAdmin):
    list_display = [field.name for field in QuestionLevel2._meta.fields]

    class Meta:
        model = QuestionLevel2


admin.site.register(QuestionLevel2, QuestionLevel2Admin)


class QuestionLevel3Admin(admin.ModelAdmin):
    list_display = [field.name for field in QuestionLevel3._meta.fields]

    class Meta:
        model = QuestionLevel3


admin.site.register(QuestionLevel3, QuestionLevel3Admin)
