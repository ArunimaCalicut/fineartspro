import random

from django.contrib import messages
from django.shortcuts import redirect, render

from artsapp.filters import StudentFilter, TeacherFilter, ProgramFilter, RegisterFilter
from artsapp.forms import Addgroup, Studentregister, Loginregister, Teacherregister, Progarmadd, update_group
from artsapp.models import Group, Student, Teacher, Program, ProgramRegistration, Result


def addgroup(request):
    form = Addgroup()
    if request.method == 'POST':
        form = Addgroup(request.POST)
        print(request.POST['name'])
        if form.is_valid():
            form.save()
            messages.info(request, "Group Added Successful")
            return redirect('group_view')
    return render(request, 'admintemp/group_add.html', {'form': form})


def group(request):
    group = Group.objects.all()
    return render(request, 'admintemp/group_view.html', {'group': group})


def group_update(request, id):
    n = Group.objects.get(id=id)
    if request.method == 'POST':
        form = update_group(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Group Updated Successfully")
            return redirect('group_view')
    else:
        form = update_group(request.POST or None, instance=n)
    return render(request, 'admintemp/group_update.html', {'form': form})


def group_delete(request, id):
    n = Group.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        return redirect('group_view')
    else:
        return redirect('group_view')


# def student_register(request):
#     login_form = Loginregister()
#     student_form = Studentregister()
#     if request.method == 'POST':
#
#         login_form = Loginregister(request.POST)
#         student_form = Studentregister(request.POST)
#         if login_form.is_valid() and student_form.is_valid():
#             g = student_form.save(commit=False)
#             student_qs = Student.objects.filter(group=g.group)
#
#             if student_qs.exists():
#                 messages.info(request, 'Student Already added for this group')
#             else:
#
#                 user = login_form.save(commit=False)
#                 user.is_student = True
#                 user.save()
#                 student = student_form.save(commit=False)
#                 student.user = user
#                 student.save()
#                 messages.info(request, 'Student Registered Successfully')
#                 return redirect('student_view')
#     return render(request, 'admintemp/student_register.html',
#                   {'login_form': login_form, 'student_form': student_form})


def student_register(request):
    login_form = Loginregister()
    student_form = Studentregister()
    context = {
        'login_form': login_form,
        'student_form': student_form
    }
    if request.method == 'POST':
        login_form = Loginregister(request.POST)
        student_form = Studentregister(request.POST)
        # print(request.POST['name'])
        if login_form.is_valid() and student_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, "Student Registered Successfull")
            return redirect('student_view')
        context = {
            'login_form': login_form,
            'student_form': student_form
        }
    return render(request, 'admintemp/student_register.html', context)


def student_view(request):
    student = Student.objects.all()
    studentFilter = StudentFilter(request.GET, queryset=student)
    student = studentFilter.qs
    context = {
        'students': student,
        'studentFilter': studentFilter,
    }
    return render(request, 'admintemp/student_view.html', context)

def student_update(request, user_id):
    n = Student.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = Studentregister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Student Updated Successfully")
            return redirect('student_view')
    else:
        form = Studentregister(request.POST or None, instance=n)
    return render(request, 'admintemp/student_update.html', {'form': form})

def student_delete(request,user_id):
    n = Student.objects.get(user_id=user_id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Student Deleted Successfully')
        return redirect('student_view')
    else:
        return redirect('student_view')


def teacher_register(request):
    login_form = Loginregister()
    teacher_form = Teacherregister()
    if request.method == 'POST':

        login_form = Loginregister(request.POST)
        teacher_form = Teacherregister(request.POST)
        if login_form.is_valid() and teacher_form.is_valid():
            g = teacher_form.save(commit=False)
            teacher_qs = Teacher.objects.filter(group=g.group)

            if teacher_qs.exists():
                messages.info(request, 'Teacher Already added for this group')
            else:

                user = login_form.save(commit=False)
                user.is_teacher = True
                user.save()
                teacher = teacher_form.save(commit=False)
                teacher.user = user
                teacher.save()
                messages.info(request, 'Teacher Registered Successfully')
                return redirect('teacher_view')
    return render(request, 'admintemp/register_teacher.html',
                  {'login_form': login_form, 'teacher_form': teacher_form})


def teacher_view(request):
    teacher = Teacher.objects.all()
    teacherFilter = TeacherFilter(request.GET, queryset=teacher)
    teacher = teacherFilter.qs
    context = {
        'teacher': teacher,
        'teacherFilter': teacherFilter,
    }
    return render(request, 'admintemp/teacher_view.html', context)

def teacher_update(request, user_id):
    n = Teacher.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = Teacherregister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Student Updated Successfully")
            return redirect('teacher_view')
    else:
        form = Teacherregister(request.POST or None, instance=n)
    return render(request, 'admintemp/teacher_update.html', {'form': form})


# def teacher_update(request,user_id):
#     n = Teacher.objects.get(user_id=user_id)
#     if request.method == 'POST':
#         form = Teacherregister(request.POST or None, instance=n)
#         if form.is_valid():
#             form.save()
#             messages.info(request, "Teacher Updated Successfully")
#             return redirect('teacher_view')
#     return render(request, 'admintemp/teacher_update.html', {'form': form})


def teacher_delete(request,user_id):
    n = Teacher.objects.get(user_id=user_id)
    if request.method == 'POST':
        n.delete()
        return redirect('teacher_view')
    else:
        return redirect('teacher_view')


def add_program(request):
    form = Progarmadd()
    if request.method == 'POST':
        form = Progarmadd(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Program Added Successfully')
            return redirect('program_view')

    return render(request, 'admintemp/program_add.html', {'form': form, })


def assign_group(request, user_id):
    student = Student.objects.get(user_id=user_id)
    groups = Group.objects.all()
    random_group = random.choice(groups)
    student.group = random_group
    student.save()
    return redirect('student_view')


def program(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET, queryset=program)
    program = programFilter.qs
    context = {
        'programs': program,
        'programFilter': programFilter,
    }
    return render(request, 'admintemp/prgm_view.html', context)


def program_update(request, id):
    obj = Program.objects.get(id=id)
    form = Progarmadd(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.info(request, 'Program Updated Successfully')
        return redirect('program_view')
    return render(request, 'admintemp/program_update.html', {'form': form})


def program_delete(request, id):
    n = Program.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Program Deleted Successfully')
        return redirect('program_view')
    else:
        return redirect('program_view')


def program_register(request):
    program = ProgramRegistration.objects.all().order_by('-submitted_date')
    registerFilter = RegisterFilter(request.GET, queryset=program)
    program = registerFilter.qs

    context = {
        'programs': program,
        'registerFilter': registerFilter,
    }
    return render(request, 'admintemp/program_register.html', context)


def result_admin(request):
    result = Program.objects.all()

    programFilter = ProgramFilter(request.GET, queryset=result)
    result = programFilter.qs

    context = {
        'results': result,
        'programFilter': programFilter,
    }

    return render(request, 'admintemp/result_list.html', context)


def results_program(request, id):
    program = Program.objects.get(id=id)
    result = Result.objects.filter(program=id).order_by('-mark')
    context = {
        'results': result,
        'program': program,

    }


def score_board(request):
    result = Group.objects.all().order_by('-total_score')

    return render(request, 'admintemp/score_board.html', {'results': result})
