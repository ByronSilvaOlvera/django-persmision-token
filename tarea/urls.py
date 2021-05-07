from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tarea import views

urlpatterns = [
    path('tarea/', views.TareaList.as_view()),
    path('tarea/<int:pk>/', views.TareaDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)