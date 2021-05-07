from django.db import models


class Vuelo(models.Model):
    created      = models.DateTimeField(auto_now_add=False)
    inicoruta    = models.CharField(max_length=100, blank=True, default='')
    destino      = models.TextField()
    cliente      = models.TextField()
    tiempovuelo  = models.TextField()
    fechallegada = models.TextField()

    class Meta   : 
        ordering = ['created']