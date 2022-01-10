import datetime
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import DateInput

from artsapp.models import Login, Group, Student, Teacher, Program, ProgramRegistration, Result


def phone_number_validator(value):
    if not re.compile(r'[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'





SEMESTER_CHOICES = (
    ('select', 'select'),
    ('First Semester', 'First Semester'),
    ('Second Semester', 'Second Semester'),
    ('Third Semester', 'Third Semester'),
    ('Fourth Semester', 'Fourth Semester'),
    ('Fifth Semester', 'Fifth Semester'),
    ('Sixth Semester', 'Sixth Semester'),
)

DEPARTMENT_CHOICES = (
    ('select', 'select'),
    ('Computer Science', 'Computer Science'),
    ('English ', 'English '),
    ('Physics', 'Physics'),
    ('Cemistry ', 'Cemistry'),
    ('Zoology ', 'Zoology'),
    ('Malayalam', 'Malayalam'),

)


class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Loginregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class Addgroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_no', 'name', 'leader_name')

    # def clean_group_no(self):
    #     group_no =self.cleaned_data['group_no']
    #     group_no_qs =Group.objects.filter(group_no=group_no)
    #
    #     if group_no_qs.exists():
    #         raise forms.ValidationError("A group with this number exists")
    #
    #
    #
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     group_name_qs = Group.objects.filter(name=name)
    #
    #     if group_name_qs.exists():
    #         raise forms.ValidationError("A group with this name  already exists")


class update_group(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_no', 'name', 'leader_name')


class Studentregister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    semester = forms.ChoiceField(choices=SEMESTER_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Student
        exclude = ('user', 'group')


    # def clean_roll_no(self):
    #     roll_no = self.cleaned_data['roll_no']
    #     roll_qs = Student.objects.filter(roll_no=roll_no)
    #     if roll_qs.exists():
    #         raise forms.ValidationError("This Roll_no Already Exist")
    #     return roll_no
    #
    # def clean_department(self):
    #     department = self.cleaned_data['department']
    #     if department == 'Select':
    #         raise forms.ValidationError("Please Select a Department")
    #     return department
    #
    # def clean_semester(self):
    #     semester = self.cleaned_data['semester']
    #     if semester == 'Select':
    #         raise forms.ValidationError("Please Select a Semester")
    #     return semester
    #
    # def clean_contact_no(self):
    #     contact_no = self.cleaned_data['contact_no']
    #     contact_no_qs_st = Student.objects.filter(contact_no=contact_no)
    #     contact_no_qs_te = Teacher.objects.filter(contact_no=contact_no)
    #
    #     if contact_no_qs_st.exists():
    #         raise forms.ValidationError("This Phone Number Already Registered")
    #     if contact_no_qs_te.exists():
    #         raise forms.ValidationError("This Phone Number Already Registered")
    #
    #     return contact_no
    #
    #
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     email_qs_st = Student.objects.filter(email=email)
    #     email_qs_te = Teacher.objects.filter(email=email)
    #     if email_qs_st.exists():
    #         raise forms.ValidationError("This email already registered")
    #     if email_qs_te.exists():
    #         raise forms.ValidationError("This email already registered")
    #     return email

# class Student_update(forms.ModelForm):
#     contact_no = forms.CharField(validators=[phone_number_validator])
#     semester = forms.ChoiceField(choices=SEMESTER_CHOICES)
#     department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
#     email = forms.CharField(validators=[
#         RegexValidator(regex='^[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
#
#     class Meta:
#         model = Student
#         exclude = ('user',)

class Teacherregister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Teacher
        exclude = ('user',)

    # def clean_roll_no(self):
    #     roll_no = self.cleaned_data['roll_no']
    #     roll_no_qs = Student.objects.filter(roll_no=roll_no)
    #     if roll_no_qs.exists():
    #         raise forms.ValidationError("This Roll_no Already Exist")
    #     return roll_no
    #
    # def clean_department(self):
    #     department = self.cleaned_data['department']
    #     if department == 'Select':
    #         raise forms.ValidationError("Please Select a Department")
    #     return department
    #
    # def clean_semester(self):
    #     semester = self.cleaned_data['semester']
    #     if semester == 'Select':
    #         raise forms.ValidationError("Please Select a Semester")
    #     return semester
    #
    # def clean_contact_no(self):
    #     contact_no = self.cleaned_data['contact_no']
    #     contact_no_qs_st = Student.objects.filter(contact_no=contact_no)
    #     contact_no_qs_te = Teacher.objects.filter(contact_no=contact_no)
    #     if contact_no_qs_st.exists():
    #         raise forms.ValidationError("This Phone Number Already Registered")
    #
    #     if contact_no_qs_te.exists():
    #         raise forms.ValidationError("This Phone Number Already Registered")
    #
    #     return contact_no
    #
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     email_qs_st = Student.objects.filter(email=email)
    #     email_qs_te = Teacher.objects.filter(email=email)
    #
    #     if email_qs_st.exists():
    #         raise forms.ValidationError("This email already registered")
    #
    #     if email_qs_te.exists():
    #         raise forms.ValidationError("This email already registered")
    #     return email

class Teacherupdate(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Teacher
        exclude = ('user',)

TYPE_CHOICES = (
    ('Individual', 'Individual'),
    ('Group', 'Group'),
)

class Progarmadd(forms.ModelForm):
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        model = Program
        fields = '__all__'

    def clean_limitation_of_participation(self):
        type = self.cleaned_data["type"]
        limit = self.cleaned_data['limitation_of_participation']
        if type == 'Individual':
            if limit > 1:
                raise forms.ValidationError('Individual Program Must have limitation of participation 1')
        return limit

class ProgramRegistrationForm(forms.ModelForm):
    submitted_date = forms.DateField(widget=DateInput)
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ProgramRegistration
        fields = ('program', 'submitted_date', 'students')

    def clean_submitted_date(self):
        date = self.cleaned_data['submitted_date']

        if date != datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date

class ResultForm(forms.ModelForm):
    mark = forms.IntegerField()

    class Meta:
        model = Result
        fields = ('program', 'student', 'mark')

    def clean(self):
        cleaned_data = super().clean()
        mark = cleaned_data.get("mark")

        if mark > 10:
            raise forms.ValidationError("Please Enter mark out of 10")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = Student.objects.none()

        if 'program' in self.data:
            try:
                program_id = int(self.data.get('program'))
                self.fields['student'].queryset = Student.objects.filter(program_registration_program_id=program_id)
            except (ValueError, TypeError):
                print('select')