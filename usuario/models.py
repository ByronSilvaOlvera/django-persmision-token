from django.db import models


class Usuario(models.Model):
    created         = models.DateTimeField(auto_now_add=False)
    nombre          = models.CharField(max_length=100, blank=True, default='')
    email           = models.TextField()
    fecha           = models.TextField()
    tiempoconectado = models.TextField()
    fechaoff        = models.TextField()

    class Meta:
        ordering = ['created']