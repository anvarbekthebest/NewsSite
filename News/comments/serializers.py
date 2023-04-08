from rest_framework import serializers
from main.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'post', 'name', 'email', 'text', 'created',)
        model = Comment
        read_only_fields = ('id', 'created',)
