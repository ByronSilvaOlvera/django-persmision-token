from rest_framework import serializers
from tarea.models import Tarea

from django.contrib.auth.models import User

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    tarea = serializers.PrimaryKeyRelatedField(many=True, queryset=Tarea.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'tarea']