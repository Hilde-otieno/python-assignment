from django.shortcuts import render

from .serializers import Class_PeriodSerializer, CourseSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import Class_Period
from course.models import Course
from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from classroom.models import Classroom
from teacher.models import Teacher
# Create your views here.

class StudentListViews(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class TeacherListViews(APIView):                                                                                                  
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
class CourseListViews(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
class ClassroomListViews(APIView):
    def get(self, request):
        Classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(Classrooms, many=True)
        return Response(serializer.data)
class Class_PeriodListViews(APIView):
    def get(self, request):
        class_periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_periods, many=True)
        return Response(serializer.data)