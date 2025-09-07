from django.urls import path
from . import views
# from transcripts_apps import views



urlpatterns = [
    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    
    # Dashboards
    path("student-dashboard/", views.student_dashboard,name="student_dashboard"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),


    # Students
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/edit/<int:student_id>/", views.student_edit, name="student_edit"),
    path("students/delete/<int:student_id>/", views.student_delete, name="student_delete"),



    # Courses
    path("courses/", views.course_list, name="course_list"),
    path("courses/add/", views.course_add, name="course_add"),
    path("courses/edit/<int:course_id>/", views.course_edit, name="course_edit"),
    path("courses/delete/<int:course_id>/", views.course_delete, name="course_delete"),


    # Grades
    path("grades/", views.grade_list, name="grade_list"),
    path("grades/add/", views.grade_add, name="grade_add"),
    path("grades/edit/<int:grade_id>/", views.grade_edit, name="grade_edit"),
    path("grades/delete/<int:grade_id>/", views.grade_delete, name="grade_delete"),


    # Transcript
    path("transcript/<int:student_id>/", views.transcript_view, name="transcript_view"),
    path("transcript/<int:student_id>/pdf/", views.transcript_pdf,
    name="transcript_pdf"),
    ]