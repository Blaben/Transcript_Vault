from django.db import models

# Create your models here.

#Students Model
class Student(models.Model):
    level_choices = [
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
    ]
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    index_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    program = models.CharField(max_length=100) # e.g. "BSc ICT"
    level = models.CharField(max_length=20, choices=level_choices) # e.g. "200"
    
    def __str__(self):
        return self.index_number
    

#Courses Model
class Course(models.Model):
    credit_choices = [
        (3, '3'),
        (6, '6'),
    ]
    course_code = models.CharField(max_length=10, unique=True)
    course_title = models.CharField(max_length=100)
    credit_hours = models.IntegerField(choices=credit_choices)

    def __str__(self):
        return self.course_title

# Grades Model
class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'), 
        ('B+', 'B+'), 
        ('B', 'B'), 
        ('C+', 'C+'),
        ('C', 'C'), 
        ('D', 'D'), 
        ('F', 'F'),
]
    level_choices = [
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
    ]

    semester_choices = [
        ('First', 'First'),
        ('Second', 'Second'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    semester = models.CharField(max_length=20, choices=semester_choices) # e.g. "First", "Second"
    level = models.CharField(max_length=20, choices=level_choices) # e.g. "100", "200"
    academic_year = models.CharField(max_length=20) # e.g. "2023/2024"
    
    def __str__(self):
        return f"{self.student.index_number} - {self.course.course_code} ({self.grade})"