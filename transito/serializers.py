from rest_framework import serializers
from transito.models import Vuelo


class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'