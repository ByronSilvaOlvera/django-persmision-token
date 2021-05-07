from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    created = models.DateTimeField(auto_now_add=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio     = models.CharField(max_length=100, blank=True, default='')
    web     = models.TextField()

    def __str__(self): 
        return self.usuario.username
   
    class Meta:
        ordering = ['created']