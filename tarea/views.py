
from tarea.models import Tarea
from tarea.serializers import TareaSerializer
from rest_framework import generics

## USER
from django.contrib.auth.models import User
from tarea.serializers import UserSerializer

## PERMISO
from rest_framework import permissions
from tarea.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class TareaList(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TareaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer