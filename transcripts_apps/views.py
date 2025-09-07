from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Student, Course, Grade
from .forms import LoginForm, StudentForm, CourseForm, GradeForm
import weasyprint


# Create your views here.

#H This view connects to the Home Page thus index.html
def home(request):
    return render(request, 'index.html')

# ---------- Auth ----------
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect("admin_dashboard")
            return redirect("student_dashboard")
    else:
        form = LoginForm()
    return render(request, "transcripts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


# ---------- Dashboards ----------
@login_required
def admin_dashboard(request): # Optional: quick stats
    context = {
        "student_count": Student.objects.count(),
        "course_count": Course.objects.count(),
        "grade_count": Grade.objects.count(),
        
        }
    
    return render(request, "transcripts/admin_dashboard.html", context)


@login_required
def student_dashboard(request):
    student = getattr(request.user, "student", None)
    return render(request, "transcripts/student_dashboard.html", {"student": student})


# Helpers
is_admin = user_passes_test(lambda u: u.is_staff)


# ---------- Student CRUD ----------
@is_admin
def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect("student_list")


@login_required
@is_admin
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "transcripts/student_form.html", {"form": form, "title": "Add Student"})


@login_required
@is_admin
def student_list(request):
    students = Student.objects.all()
    return render(request, "transcripts/student_list.html", {"students": students})


@login_required
@is_admin
def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "transcripts/student_form.html", {"form": form, "title": "Edit Student"})


# ---------- Course CRUD ----------
@login_required
@is_admin
def course_list(request):
    courses = Course.objects.all().order_by("course_code")
    return render(request, "transcripts/course_list.html", {"courses": courses})


@login_required
@is_admin
def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "transcripts/course_form.html", {"form": form, "title": "Add Course"})


@login_required
@is_admin
def course_edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
        return redirect("course_list")
    else:
        form = CourseForm(instance=course)
        return render(request, "transcripts/course_form.html", {"form": form, "title": "Edit Course"})


@login_required
@is_admin
def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect("course_list")


# ---------- Grade CRUD ----------
@login_required
@is_admin
def grade_list(request):
    grades = Grade.objects.select_related("student", "course").order_by("academic_year")
    return render(request, "transcripts/grade_list.html", {"grades": grades})

@login_required
@is_admin
def grade_add(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("grade_list")
    else:
        form = GradeForm()
    return render(request, "transcripts/grade_form.html", {"form": form,"title": "Add Grade"})

@login_required
@is_admin
def grade_edit(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grade_list")
    else:
        form = GradeForm(instance=grade)
    return render(request, "transcripts/grade_form.html", {"form": form,"title": "Edit Grade"})

@login_required
@is_admin
def grade_delete(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    grade.delete()
    return redirect("grade_list")


 # ---------- Transcript (view + PDF) ---------
@login_required
def transcript_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    grades = Grade.objects.filter(student=student).select_related("course")
    # Optional: group by semester/level in template
    return render(request, "transcripts/transcript_view.html", {"student": student, "grades": grades})

# WeasyPrint export
import weasyprint
@login_required
def transcript_pdf(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    grades = Grade.objects.filter(student=student).select_related("course")
    html = render_to_string("transcripts/transcript_pdf.html", {"student": student, "grades": grades})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'filename="transcript_{student.index_number}.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)
    return response