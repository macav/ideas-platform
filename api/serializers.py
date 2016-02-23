from api.models import Idea
from rest_framework import serializers


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea