from rest_framework import serializers
from main.models import *

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'image', 'author', 'category', 'created', 'updated', )
        model = Post
        read_only_fields = ('id', 'created', 'updated')

