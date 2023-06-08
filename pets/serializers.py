from rest_framework import serializers
from pets.models import Gender
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from .models import Pet

class PetSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    sex = serializers.ChoiceField(
        choices=Gender.choices,
        default=Gender.DEFAULT,
    )

    traits = TraitSerializer(many=True)
    group = GroupSerializer()
    
    class Meta:
        model = Pet
        fields = "__all__"
        read_only_fields = ["id"]
