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


class ProfsAdmin(admin.TabularInline):
    model = ConclusionsProfessions


class ConclusionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Conclusions._meta.fields]
    inlines = [ProfsAdmin]

    class Meta:
        model = Conclusions


admin.site.register(Conclusions, ConclusionsAdmin)


class ProfessionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Professions._meta.fields]

    class Meta:
        model = Professions


admin.site.register(Professions, ProfessionsAdmin)


class TestingResultsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TestingResults._meta.fields]
    readonly_fields = ['conc','count']

    class Meta:
        model = TestingResults


admin.site.register(TestingResults, TestingResultsAdmin)