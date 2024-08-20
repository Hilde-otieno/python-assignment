from django.shortcuts import render

from .serializers import Class_PeriodSerializer, CourseSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer, WeeklyTimetableSerializer
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
    
    
class Student_ClassDetailView(APIView):
    def get(self, request, id):
        student_class= Student.objects.get(id=id)
        serializer = StudentSerializer(student_class)
        return Response(serializer.data)
    def put(self, request, id):
        student_class = Student.objects.get(id=id)
        serializer = StudentSerializer(student_class, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student_class = Student.objects.get(id=id)
        student_class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class TeacherListViews(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        serializer = MinimalTeacherSerializer(teachers, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher= Student.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def assign_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.course.add(course)
    def assign_class(self, teacher, class_id):
        student_class = Student_Class.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class CoursesListViews(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        serializer = MinimalCourseSerializer(courses, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CoursesDetailView(APIView):
    def get(self, request, id):
        course= Courses.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class ClassPeriodListViews(APIView):
    def get(self, request):
        class_period = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_period, many=True)
        serializer = MinimalClassPeriodSerializer(class_period, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassPeriodSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        class_period= ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data)
    def put(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = StudentSerializer(class_period, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Courses.objects.get(id=course_id)
        class_period = ClassPeriod(teacher=teacher, course=course)
        class_period.save()
        return Response(status=status.HTTP_201_CREATED)
    

class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)