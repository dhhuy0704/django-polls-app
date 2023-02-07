from django.contrib import admin

from .models import Question, Choice

# If you want Choice separates with Questions, uncomment this
# And comment inlines in QuestionAdmin class.
#
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('question', 'choice_text', 'votes')

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter   = ['pub_date']
    search_fields = ['question_text']
    inlines       = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)