from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect,HttpResponse
from django.urls import reverse

from .forms import StudentForm
from .models import Student


# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        "students": Student.objects.all()
    })


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
        return render(request, 'students/add.html', {
            'form': StudentForm()
            })


def edit(request,id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.student_number =request.POST.get('student_number')
        student.first_name =request.POST.get('first_name')
        student.last_name =request.POST.get('last_name')
        student.email =request.POST.get('email')
        student.field_of_study =request.POST.get('field_of_study')
        student.gpa =request.POST.get('gpa')
        student.save()
        return redirect('/')
    else:
        student = Student.objects.get(pk = id)
        return render(request, 'students/edit.html', {'data': student})                                                                                                            


def delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return HttpResponseRedirect('index')