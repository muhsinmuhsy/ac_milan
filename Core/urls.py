from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),

    path('', views.dashbord, name='dashbord'),

    path('centers/', views.center_list, name='center_list'),
    path('centers/add/', views.center_add, name='center_add'),
    path('centers/<int:center_id>/edit/', views.center_edit, name='center_edit'),
    path('centers/<int:center_id>/delete/', views.center_delete, name='center_delete'),
    path('center_student_list/<int:center_id>/', views.center_student_list, name='center_student_list'),
    path('delete-student/<int:student_id>/', views.center_delete_student, name='center_delete_student'),

    path('students/add/', views.add_student, name='add_student'),
    path('add_student_tow', views.add_student_tow, name='add_student_tow'),
    path('student_list', views.student_list, name='student_list'),
    path('student/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('view-student/<int:student_id>/', views.view_student, name='view_student'),

    path('coordinators/', views.coordinator_list, name='coordinator_lists'),
    path('add_coordinator/', views.add_coordinator, name='add_coordinator'),
    path('coordinator/<int:coordinator_id>/edit/', views.edit_coordinator, name='edit_coordinator'),
    path('delete-coordinator/<int:coordinator_id>/', views.delete_coordinator, name='delete_coordinator'),

    path('attends_center/', views.attends_centers, name='attends_centers'),
    
    path('centers/<int:center_id>/sections/', views.center_sections, name='center_sections'),
    path('add_time_section/<int:center_id>/', views.add_time_section, name='add_time_section'),
    path('update_time_section/<int:center_id>/<int:section_id>', views.update_time_section, name='update_time_section'),
    path('delete_section/<int:center_id>/<int:section_id>/', views.delete_section, name='delete_section'),

    path('centers/<int:center_id>/timesections/<int:section_id>/addattendance/', views.add_attendance, name='add_attendance'),
    path('attendance_date/<int:center_id>/<int:section_id>/', views.attendance_date, name='attendance_date'),
    path('center/<int:center_id>/section/<int:section_id>/attendance-date/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),
    path('center/<int:center_id>/section/<int:section_id>/attendance/<int:attendance_id>/edit/', views.edit_attendance, name='edit_attendance'),
    path('center/<int:center_id>/section/<int:section_id>/attendance/<int:attendance_id>/delete/', views.delete_attendance, name='delete_attendance'),
    
]


