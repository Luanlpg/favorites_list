from django.shortcuts import render
from django.http import Http404

from .utils import EmailService

from .serializer import ClientSerializer
from .serializer import UserSerializer
from .serializer import FavoriteSerializer
from .serializer import FavoriteIdSerializer

from .models import UserModel
from .models import ClientModel
from .models import FavoriteModel

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

import time
import requests
import json

class UserView(APIView):
    """
    View que cadastra usuário.
    """
    serializer_class = UserSerializer
    email_service = EmailService()

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            time.sleep(1)
            user = UserModel.objects.get(email=request.data.dict()['email'])
            self.email_service.send_token(user.email, user.token)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientListView(APIView):
    """
    View que lista e cadastra clientes.
    """
    serializer_class = ClientSerializer

    def get(self, request, token, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(ClientModel.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, token, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(APIView):
    """
    View que mostra, altera e apaga cliente.
    """
    serializer_class = ClientSerializer

    def get_client(self, email):
        try:
            return ClientModel.objects.get(email=email)
        except ClientModel.DoesNotExist:
            raise Http404

    def get(self, request, token, email, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        client = self.get_client(email)
        serializer = self.serializer_class(client)
        return Response(serializer.data)

    def patch(self, request, token, email, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        client = self.get_client(email)
        serializer = self.serializer_class(client, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, token, email, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        client = self.get_client(email)
        client.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FavoritesListView(APIView):
    """
    View que lista e cadastra favoritos.
    """
    serializer_class = FavoriteSerializer
    id_serializer_class = FavoriteIdSerializer

    def get_client(self, email):
        try:
            return ClientModel.objects.get(email=email)
        except ClientModel.DoesNotExist:
            raise Http404

    def get(self, request, token, email, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        client = self.get_client(email)
        serializer = self.serializer_class(FavoriteModel.objects.filter(id_client=client.id), many=True)
        return Response(serializer.data)

    def post(self, request, token, email, format=None):
        try:
            UserModel.objects.get(token=token)
        except UserModel.DoesNotExist:
            return Response(json.dumps({"token":"Não autorizado."}), status=status.HTTP_404_NOT_FOUND)

        client = self.get_client(email)
        id_serializer = self.id_serializer_class(data=request.data)

        if id_serializer.is_valid():
            try:
                response = requests.get(f'http://challenge-api.luizalabs.com/api/product/{request.data.dict()["id"]}')

                FavoriteModel.objects.create(
                    id = response.json()['id'],
                    id_client = client.id,
                    title = response.json()['title'],
                    price = response.json()['price'],
                    image = response.json()['image'],
                    brand = response.json()['brand']
                )
            except Exception as e:
                return Response(json.dumps({"id":"Produto não encontrado."}), status=status.HTTP_404_NOT_FOUND)
            return Response(id_serializer.data, status=status.HTTP_201_CREATED)
        return Response(id_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
