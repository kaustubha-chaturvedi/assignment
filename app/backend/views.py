from backend.models import *
from backend.forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.forms import ValidationError
from django.utils.encoding import smart_str
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes

def home(request):
    return render(
        request,
        "home.html",
        {"teachers": Teacher.objects.all(), "students": Student.objects.all()},
    )

@api_view(["GET"])
def get_teachers(request):
    student = get_object_or_404(Student, id=request.GET["student"])
    teachers = student.teachers.values('id', 'name')
    response =""
    if not teachers:
        return HttpResponse('<option value="" selected disabled>No Teachers Alloted</option>')
    for teacher in list(teachers):
        response += f'<option value="{teacher["id"]}">{teacher["name"]}</option>\n'
    return HttpResponse(response)

@api_view(["GET"])
def get_students(request):
    teacher = get_object_or_404(Teacher, id=request.GET["teacher"])
    students = Student.objects.filter(teachers=teacher).values('id', 'name')
    response =""
    if not students:
        return HttpResponse('<option value="" selected disabled>No Students Alloted</option>')
    for student in list(students):
        response += f'<option value="{student["id"]}">{student["name"]}</option>\n'
    return HttpResponse(response)

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def generate_certificate(request):
    if request.method == "POST":
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            student = form.cleaned_data['student']
            teacher = form.cleaned_data['teacher']
            certificate = Certificate.objects.filter(student=student, teacher=teacher).first()

            if not certificate:
                certificate = Certificate(student=student, teacher=teacher)
                certificate.save()

            token = certificate.generate_jwt(user=request.user)

            response = HttpResponse(content_type='application/jwt')
            response['Content-Disposition'] = f'attachment; filename="{smart_str("token.jwt")}"'
            response.write(token)
            return response
    return redirect("home")

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def verify_certificate(request):
    if request.method == 'POST':
        token_file = request.FILES.get('token_file')

        if token_file:
            try:
                file_path = default_storage.save('uploaded_tokens/token.jwt', ContentFile(token_file.read()))
                with default_storage.open(file_path) as file:
                    token_content = file.read()
                is_valid, certificate = Certificate.verify_jwt(token_content)

                if is_valid:
                    return render(request, 'certificate.html', {
                        'teacher': certificate.teacher.name,
                        'student': certificate.student.name,
                        'issue_date': certificate.issue_date.strftime('%Y-%m-%d %H:%M'),
                        'expiry_date': certificate.expiry_date.strftime('%Y-%m-%d %H:%M')
                    })
                else:
                    return HttpResponse("Invalid Token or Certificate has expired.")
            except ValidationError as e:
                return HttpResponse(f"Error: {e}")

    return render(request, "verify.html")

@login_required
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"added teacher")
            return redirect("home")
    else:
        form = TeacherForm()

    return render(request, 'add.html', {'form': form})


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            teachers = form.cleaned_data.get("teachers")
            user.teachers.set(teachers)
            messages.success(request,"added student")
            return redirect("home")

    else:
        form = StudentForm()
    return render(request, "add.html", {"form": form})
