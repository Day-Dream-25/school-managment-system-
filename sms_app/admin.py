from django.contrib import admin

# Register your models here.
from sms_app.models import User, School, Teacher, Student


# class UserAdmin(admin.TabularInline):
#     model = User
#
# class SchoolAdmin(admin.ModelAdmin):
#    inlines = [U,]

admin.site.register(User)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)

