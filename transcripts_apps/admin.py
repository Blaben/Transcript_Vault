from django.contrib import admin
from .models import Student, Course, Grade

# Register your models here.

#Student model successfully registered here
class StudentAdmin(admin.ModelAdmin):
    list_display = ("index_number", "first_name", "last_name", "program", "level")
    search_fields = ("index_number", "first_name", "last_name", "program")

admin.site.register(Student, StudentAdmin)


# Course model successfully registered here
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_code", "course_title", "credit_hours")
    search_fields = ("course_code", "course_title")

admin.site.register(Course, CourseAdmin)


# Grade model successfully registered here
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "grade", "semester", "level", "academic_year")
    list_filter = ("semester", "level", "academic_year", "grade")
    search_fields = ("student__index_number", "course__course_code")

admin.site.register(Grade, GradeAdmin)
