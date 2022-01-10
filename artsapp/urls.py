from django.urls import path

from artsapp import views, admin_views, student_views, teacher_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('admin_home/', views.admin_home, name='admin_home'),


    path('group_add/', admin_views.addgroup, name='group_add'),
    path('group_view/', admin_views.group, name='group_view'),
    path('group_update/<int:id>/', admin_views.group_update, name='group_update'),
    path('group_delete/<int:id>/', admin_views.group_delete, name='group_delete'),
    path('student_register/', admin_views.student_register, name='student_register'),
    path('student_view/',admin_views.student_view,name ='student_view'),
    path('student_update/<int:user_id>/', admin_views.student_update, name='student_update'),
    path('student_delete/<int:user_id>/', admin_views.student_delete, name='student_delete'),
    path('teacher_register/', admin_views.teacher_register, name='teacher_register'),
    path('teacher_view/', admin_views.teacher_view, name='teacher_view'),
    path('teacher_update/<int:user_id>/', admin_views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:user_id>/', admin_views.teacher_delete, name='teacher_delete'),
    path('assign_group/<int:user_id>/', admin_views.assign_group, name='assign_group'),
    path('program_view/', admin_views.program, name='program_view'),
    path('program_add/', admin_views.add_program, name='program_add'),
    path('program_update/<int:id>/', admin_views.program_update, name='program_update'),
    path('program_delete/<int:id>', admin_views.program_delete, name='program_delete'),
    path('program_register/', admin_views.program_register, name='program_register'),
    path('result_list/', admin_views.result_admin, name='result_list'),
    path('result_program/', admin_views.results_program, name='result_program'),
    path('score_board/', admin_views.score_board, name='score_board'),


    path('student_home/', student_views.student_home, name='student_home'),
    path('team/', student_views.teams_views_student, name='team'),
    path('prgm_view/',student_views.program_views_student, name='prgm_view'),
    path('scorebord_s/', student_views.scoreboard_s, name='scorebord_s'),


    path('teacher_home/', teacher_views.teacher_home, name='teacher_home'),
    path('teams/',teacher_views.teams,name='teams'),
    path('program/',teacher_views.program_view_teacher,name='program'),
    path('program_update/<int:id>/',teacher_views.program_update_teacher,name='program_update'),
    path('register_teacher/',teacher_views.register_teacher,name='register_teacher'),
    path('program_result/', teacher_views.program_result, name='program_result'),
    # path('result_add2/', teacher_views.add_result, name='result_add2'),
    path('scoreboard/', teacher_views.scoreboard_t, name='scoreboard'),

]