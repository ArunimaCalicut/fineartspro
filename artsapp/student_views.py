from django.shortcuts import render

from artsapp.filters import StudentFilter, ProgramFilter
from artsapp.models import Student, Program, ProgramRegistration, Group


def student_home(request):
    return render(request,'student/student_home.html')

def teams_views_student(request):
    student = Student.objects.get(user=request.user)
    team = Student.objects.filter(group=student.group)
    groupFilter = StudentFilter(request.GET, queryset = team)
    team = groupFilter.qs
    context = {
        'team':team,
        'groupFilter':groupFilter
    }
    return render(request,'student/team.html', context)

def program_views_student(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET, queryset = program)
    program= ProgramFilter.qs
    context = {
        'program':program,
        'programFilter':programFilter
    }
    return render(request,'student/prgm_view.html',context)



def registered_programs(request):
    student = Student.objects.get(user=request.user)
    program = ProgramRegistration.objects.filter(students__student=student)

    context = {
        'programs': program,
    }
    return render(request, 'student/registered_programs.html', context)

def result_student(request):
    result = Program.objects.all()
    programFilter = ProgramFilter(request.GET,queryset=result)
    result = ProgramFilter.qs
    context = {
        'result':result,
        'programFilter':programFilter
    }
    return render(request,'student/result_list.html',context)

def scoreboard_s(request):
    result = Group.objects.all().order_by('-total_score')
    return render(request, 'student/scorebord_s.html', {'results': result})