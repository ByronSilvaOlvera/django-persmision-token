
from perfiles.models import Perfil
from perfiles.serializers import PerfilSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

#authenticacion
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#PERMISSION
from rest_framework.permissions import IsAdminUser

class PerfilList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = User.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):        
        queryset = self.get_queryset().values_list('username','email')
        serializer = PerfilSerializer(queryset, many=True)
        return Response(serializer.data)


class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PerfilSerializer
