from chat.serializers import MessageSerializer, MessagePostSerializer
from chat.models import Message

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class MessageView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        messages = Message.objects.filter(sender_id=request.user.id).order_by('id')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessagePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MessageDetailView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        message = get_object_or_404(Message, pk=pk, sender_id=request.user.id)
        if not message.message_read:
            message.message_read = True
        message.save()
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        message = get_object_or_404(Message, pk=pk)
        if request.user.id != message.sender.id and request.user.id != message.receiver.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UnReadMessageView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        messages = Message.objects.filter(sender_id=request.user.id, message_read=False).order_by('id')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)