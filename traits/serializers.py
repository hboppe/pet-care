from rest_framework import serializers
from .models import Trait

class TraitSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Trait
        field = "__all__"
        read_only_fields = ["id"]

