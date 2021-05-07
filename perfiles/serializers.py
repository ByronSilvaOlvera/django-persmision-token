from rest_framework import serializers
from perfiles.models import Perfil
from django.contrib.auth.models import User


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #('username','email','first_name','last_name','password1','password2')