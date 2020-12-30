from django.db import models
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User


class School_User(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'
    PROFESSION_CHOICES = [
        (TEACHER, 'TEACHER'),
        (STUDENT, 'STUDENT'),
    ]
    profession = models.CharField(max_length=12, choices=PROFESSION_CHOICES)

    def __str__(self):
        return self.name

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_number(number, password):
        return School_User.objects.get(number=number, password=password)


class Project(models.Model):
    project_name = models.CharField(max_length=25, unique=True)
    project_detail = models.CharField(max_length=150)
    date_of_submission = models.DateTimeField()

    def __str__(self):
        return self.project_name


class Project_assign(models.Model):
    Projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    Students = models.ForeignKey(School_User, on_delete=models.CASCADE, limit_choices_to={'profession': 'STUDENT'})
    UNATTEMPTED = 'UNATTEMPTED'
    SUBMITTED = 'SUBMITTED'
    APPROVED = 'APPROVED'
    UNAPPROVED = 'UNAPPROVED'
    STATUS_CHOICES = [
        (UNATTEMPTED, 'UNATTEMPTED'),
        (SUBMITTED, 'SUBMITTED'),
        (APPROVED, 'APPROVED'),
        (UNAPPROVED, 'UNAPPROVED'),
    ]
    project_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=UNATTEMPTED)
    submission_link = models.CharField(max_length=150, default='', null=True, blank=True)

    def st_name(self):
        return self.Students.name

    def pr_name(self):
        return self.Projects.project_name

    @staticmethod
    def return_project_assign(us_id):
       return Project_assign.objects.filter(Students_id=us_id)

    def __str__(self):
        a = self.Students.name
        b = self.Projects.project_name
        c = self.project_status
        d = self.Projects.date_of_submission
        return "This Project "+b+" has been assigned to "+a+" and the status is "+c+" and the last dat is "+str(d)
        

    def submit(link):
        Project_assign.submission_link = link
        Project_assign.project_status = "SUBMITTED"

    def approve(self):
        self.project_status = APPROVED
