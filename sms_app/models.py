from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    Roll_Choices = (
        ("SCHOOL", "SCHOOL"),
        ("TEACHER", "TEACHER"),
        ("STUDENT", "STUDENT"),

    )

    phone_no = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50, blank=True)
    roll = models.CharField(
        max_length=20,
        choices=Roll_Choices, default="STUDENT"
    )

    def __str__(self):
        return str(self.username)

    @property
    def category_id(self):
        import pdb; pdb.set_trace()
        data = {
            "student": Student.objects.all(),
            "teacher": Teacher.objects.all(),
            "school": School.objects.all()
        }
        return data.get(self.roll.lower()).filter(user_id=self.id).first()


class School(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, null=True, related_name='school')
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)


class Teacher(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, null=True, related_name='teacher')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    birthdate = models.DateField(max_length=8, null=True, blank=True)
    subject = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, null=True, related_name='student')
    teacher = models.ManyToManyField(Teacher)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    birthdate = models.DateField(max_length=8, null=True, blank=True)
    standard = models.IntegerField()

    def __str__(self):
        return str(self.id)

