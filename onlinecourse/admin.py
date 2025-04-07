from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5
    inlines = [ChoiceInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'course', 'grade')
    list_filter = ['course']
    search_fields = ['content']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'question', 'is_correct')
    list_filter = ['question']
    search_fields = ['content']

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'get_choices')
    list_filter = ['enrollment__course']
    search_fields = ['enrollment__user__username']

    def get_choices(self, obj):
        return ", ".join([choice.content for choice in obj.choices.all()])
    get_choices.short_description = 'Selected Choices'

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# <HINT> Register Question and Choice models here
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
