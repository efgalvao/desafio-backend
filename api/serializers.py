from rest_framework import serializers
from .models import Viagem


class ViagemSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Viagem
        fields = ['id', 'data_inicio', 'data_fim', 'classificacao', 'nota']
