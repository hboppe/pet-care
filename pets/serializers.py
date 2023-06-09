from rest_framework import serializers
from pets.models import Gender
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from .models import Pet
from groups.models import Group

class PetSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Gender.choices,
        default=Gender.DEFAULT
    )

    group = GroupSerializer()
    traits = TraitSerializer(many=True)
