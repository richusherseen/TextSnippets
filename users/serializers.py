from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Snippets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class SnippetSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=30)
    text = serializers.CharField(required=True, max_length=80)
    

    


