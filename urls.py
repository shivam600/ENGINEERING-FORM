from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.add_student,name='add_student'),
    path("show_student",views.show_student,name="show_student"),
    path("<int:id>/",views.add_student,name="students_update"),
    path("delete/<int:id>/",views.student_delete,name="students_delete"),
    # path("password/"),
    
]
