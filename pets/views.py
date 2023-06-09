from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from .serializers import PetSerializer
from groups.models import Group
from traits.models import Trait
from pets.models import Pet
import ipdb


class PetView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()
        result_page = self.paginate_queryset(pets, request)

        pets_serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(pets_serializer.data)

    def post(self, request: Request) -> Response:
        pet_serializer = PetSerializer(data=request.data)

        pet_serializer.is_valid(raise_exception=True)


        group_data = pet_serializer.validated_data.pop("group")
        traits_data = pet_serializer._validated_data.pop("traits")

        pet_group, created = Group.objects.get_or_create(**group_data)

        pet_traits_list = []

        for trait in traits_data:
            found_trait = Trait.objects.filter(name__iexact=trait["name"]).first()
            if not found_trait:
                found_trait, created = Trait.objects.get_or_create(**trait)
            pet_traits_list.append(found_trait)

        new_pet = Pet.objects.create(**pet_serializer.validated_data, group=pet_group)

        new_pet.traits.set(pet_traits_list)

        pet_serializer = PetSerializer(new_pet)

        return Response(pet_serializer.data, status.HTTP_201_CREATED)
