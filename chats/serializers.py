from chats.models import Message
from rest_framework import serializers
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp', 'is_read']
