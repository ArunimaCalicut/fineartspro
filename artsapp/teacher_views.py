from django.contrib import messages
from django.shortcuts import render, redirect

from artsapp.filters import GroupFilter, ProgramFilter, RegisterFilter
from artsapp.forms import Progarmadd, ProgramRegistrationForm
from artsapp.models import Student, Program, ProgramRegistration, Result, Group


def teacher_home(request):
    return render(request,'teacher/teacher_home.html')

def teams(request):
    team = Student.objects.all().order_by('group')
    groupFilter = GroupFilter(request.GET , queryset=team)
    team = groupFilter.qs
    context = {
        'team':team,
        'groupFilter':groupFilter
    }
    return render(request,'teacher/teams.html',context)

def program_view_teacher(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET,queryset=program)
    program = ProgramFilter.qs
    context = {
        'program':program,
        'programFilter':programFilter
    }
    return render(request,'teacher/program.html',context)

def program_update_teacher(request,id):
    n = Program.objects.get(id=id)
    form = Progarmadd(request.POST or None,instance=n)
    if form.is_valid():
        form.save()
        messages.info(request, "Program Updated Successfully")
        return redirect("program")
    return render(request, 'teacher/program_update.html', {'form': form})

def register_teacher(request):
    program = ProgramRegistrationForm.objects.all().order_by('-submitted_date')
    registerFilter = RegisterFilter(request.GET, queryset=program)
    program = RegisterFilter.qs
    context = {
        'program':program,
        'registerFilter':registerFilter
    }
    return render(request,'teacher/register_teacher.html', context)

def program_result(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET, queryset=program)
    program = programFilter.qs
    context = {
        'program': program,
        'programFilter': programFilter,
    }
    return render(request, 'teacher/program_result.html', context)

def scoreboard_t(request):
    result = Group.objects.all().order_by('-total_score')
    return render(request, 'teacher/scoreboard.html', {'results': result})
