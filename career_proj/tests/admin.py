from django.contrib import admin
from .models import Tests,Question, UserResponse

admin.site.register(Tests)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'section', 'correct_option')
    list_filter = ('section',)
    search_fields = ('text',)

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'selected_option', 'score', 'section')
    list_filter = ('section', 'user')
    search_fields = ('user__username', 'question__text')

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse, UserResponseAdmin)