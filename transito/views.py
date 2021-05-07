
from transito.models import Vuelo
from transito.serializers import VueloSerializer
from rest_framework import generics

#Permission
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class VueloList(generics.ListCreateAPIView):
    queryset           = Vuelo.objects.all()
    serializer_class   = VueloSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
  
 
class VueloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  
