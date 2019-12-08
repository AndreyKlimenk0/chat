from chat.models import Message
from rest_framework.serializers import ModelSerializer


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessagePostSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'message']