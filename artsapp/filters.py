import django_filters
from django import forms
from django_filters import CharFilter
from artsapp.models import Student, Teacher, Program, ProgramRegistration


class StudentFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Student', 'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('name',)

class TeacherFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Teacher', 'class': 'form-control'}))

    class Meta:
        model = Teacher
        fields = ('name',)

class ProgramFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Program ', 'class': 'form-control'}))

    class Meta:
        model = Program
        fields = ('name',)

class RegisterFilter(django_filters.FilterSet):
    class Meta:
        model = ProgramRegistration
        fields = ('program',)

class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ('group',)