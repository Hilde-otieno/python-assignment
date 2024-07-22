from django.urls import path
from .views import Class_PeriodListViews, CourseListViews, ClassroomListViews, StudentDetailView, StudentListViews , TeacherListViews, TeacherDetailView, CourseDetailView, Class_PeriodDetailView, ClassroomDetailView

urlpatterns = [
    path("Students/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teachers/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Course/",CourseListViews.as_view(),name = "course_list_view"),
    path("Classroom/",ClassroomListViews.as_view(),name = "class_room_list_view"),
    path("class_period/",Class_PeriodListViews.as_view(),name = "class_period_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(), name= "student_detail_view"),
    path ("teachers/<int:id>/", TeacherDetailView.as_view(), name = "teacher_detail_"),
    path ("courses/<int:id>/", CourseDetailView.as_view(), name = "course_detail_"),
    path ("class_period/<int:id>/", Class_PeriodDetailView.as_view(), name = "class_period_detail_"),
    path ("classroom/<int:id>/", ClassroomDetailView.as_view(), name = "classroom_detail_")
]