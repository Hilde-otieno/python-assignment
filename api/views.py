from django.shortcuts import render

from .serializers import Class_PeriodSerializer, CourseSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import Class_Period
from rest_framework import status
from course.models import Course
from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from classroom.models import Classroom
from teacher.models import Teacher
# Create your views here.



class TeacherListViews(APIView):                                                                                                  
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.Save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self,request,id):
        teacher =Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.Save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher =Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
class CourseListViews(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CourseSerializer(Course,many=True)
        if serializer.is_valid():
            serializer.Save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,id):
        course =Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.Save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassroomListViews(APIView):
    def get(self, request):
        Classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(Classrooms, many=True)
        return Response(serializer.data)
    
class ClassroomDetailView(APIView):
    def get(self,request):
        classroom=Classroom.objects.get(id=id)
        Serializer = ClassroomSerializer(classroom)
        return Response(Serializer.data)
    def put(self,request,id):
        classroom=Classroom.objects.get(id=id)
        serializer=ClassroomSerializer(classroom,data=request.data)
        if serializer.is_valid():
            serializer.Save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_201_BAD_REQUEST)
    

    def delete(self,request,id):
        classroom =Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class Class_PeriodListViews(APIView):
    def get(self, request):
        class_periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_periods, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)

class Class_PeriodDetailView(APIView):
    def get(self,request,id):
        class_period=Class_Period.objects.get(id=id)
        Serializer = Class_PeriodSerializer(class_period)
        return Response(Serializer.data)
    def put(self,request,id):
        class_period=Class_Period.objects.get(id=id)
        serializer =Class_PeriodSerializer(class_period,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        class_period=Class_Period.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
class StudentListViews(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.Save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
