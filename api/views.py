from django.shortcuts import render
from api.serializer import Class_PeriodSerializer, CourseSerializer, Student_ClassSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import Class_Period
from course.models import Course
from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from classroom.models import Student_Class
from teacher.models import Teacher
# Create your views here.

class StudentListViews(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
class Teacher                                                                                                           ListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
class ClassListViews(APIView):
    def get(self, request):
        student_class = Student_Class.objects.all()
        serializer = Student_ClassSerializer(student_class, many=True)
        return Response(serializer.data)
class Class_PeriodListViews(APIView):
    def get(self, request):
        class_period = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_period, many=True)
        return Response(serializer.data)