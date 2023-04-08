from rest_framework import serializers
from main.models import *

class TopPostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'created', 'updated',)
        model = TopPost
        read_only_fields = ('id', 'created', 'updated')

