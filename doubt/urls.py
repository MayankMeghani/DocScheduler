from django.urls import path
from . import views

app_name = 'doubt'

urlpatterns = [
    path('doubt/list', views.doubt_list, name='doubt_list'),
    path('home_patient/doubt', views.user_doubts, name='user_doubts'),
    path('home_doctor/doubt', views.solved_doubts, name='solved_doubts'),
    path('doubt/create', views.doubt_create, name='doubt_create'),
    path('<int:doubt_id>/', views.doubt_solution, name='doubt_solution'),
    path('update_doubt/<int:doubt_id>/', views.update_doubt, name='update_doubt'),
    path('delete_doubt/<int:doubt_id>/', views.delete_doubt, name='delete_doubt'),
    path('create_solution/<int:doubt_id>', views.create_solution, name='create_solution'),
    path('update_solution/<int:solution_id>/', views.update_solution, name='update_solution'),
    path('delete_solution/<int:solution_id>/', views.delete_solution, name='delete_solution'),
]
