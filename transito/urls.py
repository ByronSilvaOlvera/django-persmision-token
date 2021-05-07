from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from transito import views

urlpatterns = [
    path('transito/', views.VueloList.as_view()),
    path('transito/<int:pk>/', views.VueloDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)