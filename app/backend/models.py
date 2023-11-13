from django.db import models
from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

class Teacher(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher, blank=True, related_name='student_teachers')

    def __str__(self):
        return self.name

class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=(timezone.now() + timedelta(days=180)))

    def __str__(self):
        return f"{self.teacher.name} - {self.student.name} - {self.issue_date}"

    def generate_jwt(self,user):
        refresh = RefreshToken.for_user(user)
        refresh.payload['cert_id'] = self.pk
        return str(refresh.access_token)

    @staticmethod
    def verify_jwt(token):
        try:
            access_token = AccessToken(token)
            certificate =  Certificate.objects.get(id=access_token.payload.get('cert_id'))
            current_time = timezone.now()

            if current_time > certificate.expiry_date:
                return False, None
            else:
                return True, certificate

        except Exception as e:
            return False, None 