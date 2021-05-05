from django.db import models


class Tarea(models.Model):
    created     = models.DateTimeField(auto_now_add=False)
    titulo      = models.TextField(max_length=100, blank=True, default='')
    descripcion = models.TextField()
    estado      = models.TextField()
    fechaoff    = models.TextField()
    owner       = models.ForeignKey('auth.User', related_name='tarea', on_delete=models.CASCADE) 
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']
    