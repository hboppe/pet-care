from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ["id", "created_at"]