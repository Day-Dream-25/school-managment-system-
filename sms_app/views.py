import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from sms_app.forms import UserForm, SchoolForm, TeacherForm, StudentForm, LoginForm
from sms_app.models import User, School, Teacher, Student
from django.conf import settings
from django.core.mail import send_mail



class UserRegistration(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserForm
    success_url = "login/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        if user.roll == "SCHOOL":
            return redirect("school")
        elif user.roll == "TEACHER":
            return redirect("teacher")
        elif user.roll == "STUDENT":
            return redirect("student")

        return super(UserRegistration, self).form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ['address', 'phone_no', 'roll']
    template_name = 'update.html'
    # success_url = "/updateschool/"

    def get_success_url(self):
        if self.request.user.roll == 'STUDENT':
            return reverse('detailstudent', kwargs={"pk": self.request.user.category_id.id})

            # return 'detailstudent' + '/' + str(self.request.user.category_id)
        if self.request.user.roll == 'SCHOOL':
            return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})

            # return '/login/detailschool' + '/' + str(self.request.user.category_id)
        if self.request.user.roll == 'TEACHER':
            return reverse('detailteacher', kwargs={"pk": self.request.user.category_id.id})

            # return '/login/detailteacher' + '/' + str(self.request.user.category_id)


class SchoolView(CreateView):
    template_name = 'school.html'
    model = School
    form_class = SchoolForm
    success_url = "/login/"

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        form.save()
        return super().form_valid(form)


class StudentView(CreateView):
    template_name = 'student_home.html'
    model = Student
    # form_class = StudentForm
    fields = (
        'user', 'teacher', 'school', 'birthdate', 'standard'
    )
    success_url = "/login/"


class SchoolDetailView(ListView):
    model = School
    template_name = 'school_home.html'


class SchoolUpdateView(UpdateView):
    model = School
    fields = '__all__'
    template_name = 'update.html'

    def put(self, *args, **kwargs):
        import pdb
        pdb.set_trace()

    def get_success_url(self):
        return reverse('updateschool', kwargs={"pk": self.request.user.category_id.id})
        # return 'updateschool' + '/' + str(self.request.user.category_id)


class SchoolDeleteView(DeleteView):
    template_name = 'school.html'


class TeacherView(CreateView):
    template_name = 'teacher_home.html'
    model = Teacher
    form_class = TeacherForm
    success_url = "/login/"


class TeacherDetailView(ListView):
    model = Teacher
    template_name = 'teacher.html'
    def get_queryset(self):
        return Teacher.objects.filter(school_id=self.request.user.category_id)


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = 'update.html'
    success_url = "/teacherdetail/"

    def get_success_url(self):
        import pdb
        pdb.set_trace()
        if not self.request.GET.get('school'):
            return reverse('updateteacher', kwargs={"pk": self.request.user.category_id})
        return self.success_url

            # return 'updateteacher' + '/' + str(self.request.user.category_id)


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'delete_teacher.html'

    def get_success_url(self):
        # return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})

        return 'detailschool' + '/' + str(self.request.user.category_id)


class StudentDetailView(ListView):
    model = Student
    template_name = 'student.html'

    def get_queryset(self):
        return Student.objects.filter(school_id=self.request.user.category_id)


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('school',  'birthdate', 'standard')
    template_name = 'update.html'

    def get_success_url(self):

        if self.request.user.roll == 'STUDENT':
            return reverse('updatestudent', kwargs={"pk": self.request.user.category_id.id})
            # return HttpResponseRedirect(reverse('updatestudent', kwargs={"pk": self.request.user.category_id.id}))
            # return 'updatestudent' + '/' + str(self.request.user.category_id)
        if self.request.user.roll == 'SCHOOL':
            return reverse('updateschool', kwargs={"pk": self.request.user.category_id.id})
            # return 'updateschool' + '/' + str(self.request.user.category_id)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_teacher.html'

    def get_success_url(self):
        return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})

        # return 'detailschool' + '/' + str(self.request.user.category_id)


class UserLogin(LoginView):
    template_name = 'login.html'
    # form_class = LoginForm
    # import pdb;pdb.set_trace()

    def form_valid(self, form):
        # import pdb
        # pdb.set_trace()
        super(UserLogin, self).form_valid(form)
        user = form.get_user()
        # import pdb;pdb.set_trace()
        if user.roll.lower() == "student":
            # otp = random.randint(1000,9999)
            # send_mail(
            #     'Subject here',
            #     'Here is the message.'+str(otp),
            #     'dharti.pysquad@gmail.com',
            #     ['dharti.pysquad@gmail.com'],
            #     fail_silently=False,
            # )
            return HttpResponseRedirect(reverse('detailstudent', kwargs={"pk": user.category_id.id}))
        elif user.roll.lower() == "school":
            return HttpResponseRedirect(reverse('detailschool', kwargs={"pk": user.category_id}))
        elif user.roll.lower() == "teacher":
            return HttpResponseRedirect(reverse('detailteacher', kwargs={"pk": user.category_id.id}))

    # success_url = '/'


    # def form_valid(self, form):
    #     # import pdb;pdb.set_trace()
    #     super().form_valid(form)
    #     user = form.get_user()
    #     if user.roll == "SCHOOL":
    #         return redirect("school")
    #     elif user.roll == "TEACHER":
    #         return redirect("teacher")
    #     elif user.roll == "STUDENT":
    #         return redirect("student")


class Teacher_DetailView(DetailView):
    model = Teacher
    template_name = 'detail.html'


class Student_DetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

    def get_context_data(self, **kwargs):
        # import pdb
        # pdb.set_trace()
        context = super().get_context_data(**kwargs)
        teachers = Teacher.objects.filter(student=self.get_object().id)
        context['teachers'] = teachers
        return context


class School_DetailView(DetailView):
    model = School
    template_name = 'school_detail.html'


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")
