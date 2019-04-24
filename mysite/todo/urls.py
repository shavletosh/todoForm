from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('todo/<int:pk>/', views.TodoDetail, name='TodoDetail'),
	path('todo/new/', views.TodoNew, name='TodoNew'),
	path('todo/<int:pk>/edit>', views.TodoEdit, name='TodoEdit'),
]
