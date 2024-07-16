from django.urls import path
from .views import Class_PeriodListViews, CourseListViews, ClassroomListViews, StudentListViews , TeacherListViews

urlpatterns = [
    path("Students/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teachers/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Course/",CourseListViews.as_view(),name = "course_list_view"),
    path("Classroom/",ClassroomListViews.as_view(),name = "class_room_list_view"),
    path("Class_Period/",Class_PeriodListViews.as_view(),name = "class_period_list_view")
]