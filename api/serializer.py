from rest_framework import serializers

from .models import UserModel
from .models import ClientModel
from .models import FavoriteModel


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializador de clientes.
    """
    class Meta:
        model = ClientModel
        depth = 1
        fields = [
            'name',
            'email'
            ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador de clientes.
    """
    class Meta:
        model = UserModel
        depth = 1
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
            ]


class FavoriteIdSerializer(serializers.ModelSerializer):
    """
    Serializador de id favoritos.
    """
    class Meta:
        model = FavoriteModel
        depth = 1
        fields = [
            'id'
            ]


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializador de favoritos.
    """
    class Meta:
        model = FavoriteModel
        depth = 1
        fields = [
            'id',
            'title',
            'price',
            'image',
            'brand'
            ]
