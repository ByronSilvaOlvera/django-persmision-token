from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from perfiles import views

from rest_framework  import authtoken

urlpatterns = [
    path('perfil/', views.PerfilList.as_view()),
    path('perfil/<int:pk>/', views.PerfilDetail.as_view()),
    path('perfil/api-token-auth/', authtoken.views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)