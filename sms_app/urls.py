from django.urls import path

from sms_app.views import UserRegistration, SchoolView, TeacherView, StudentView, UserLogin, SchoolUpdateView, \
    SchoolDetailView, TeacherDetailView, StudentDetailView, TeacherUpdateView, TeacherDeleteView, StudentUpdateView, \
    StudentDeleteView, Teacher_DetailView, Student_DetailView, School_DetailView, UserUpdateView,Logout

urlpatterns = [
    path('', UserRegistration.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),


    path('school/', SchoolView.as_view(), name="school"),
    path('teacher/', TeacherView.as_view(), name="teacher"),
    path('student/', StudentView.as_view(), name="student"),

    path('schooldetail/<int:pk>/', SchoolDetailView.as_view(), name='schooldetail'),
    path('teacherdetail/', TeacherDetailView.as_view(), name='teacherdetail'),
    path('studentdetail/', StudentDetailView.as_view(), name='studentdetail'),

    path('schoolupdate/<int:pk>/', SchoolUpdateView.as_view(), name="updateschool"),
    path('teacherupdate/<int:pk>/', TeacherUpdateView.as_view(), name='updateteacher'),
    path('studentupdate/<int:pk>/', StudentUpdateView.as_view(), name='updatestudent'),

    path('teacherdelete/<int:pk>/', TeacherDeleteView.as_view(), name='deleteteacher'),
    path('studentdelete/<int:pk>/', StudentDeleteView.as_view(), name='deletestudent'),

    path('detailteacher/<int:pk>/', Teacher_DetailView.as_view(), name='detailteacher'),
    path('detailstudent/<int:pk>/', Student_DetailView.as_view(), name='detailstudent'),
    path('detailschool/<int:pk>/', School_DetailView.as_view(), name='detailschool'),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='updateuser'),

]
