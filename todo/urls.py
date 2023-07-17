from django.urls import path
from . import views

urlpatterns = [
	path('todo/', views.todo_view, name = 'todo'),
	path('delete/<int:id>/', views.task_delete, name = 'task_delete'),
	path('completed/<int:id>/', views.task_completed, name = 'task_completed'),
	path('update/<int:id>/', views.task_update, name = 'task_update'),
]