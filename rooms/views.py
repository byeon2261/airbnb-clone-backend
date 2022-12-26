from rest_framework.views import APIView
from django.db import transaction
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Amenity, Room
from categories.models import Category
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            serializer = AmenitySerializer(amenity)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            serializer = AmenitySerializer(updated_amenity)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_room = Room.objects.all()
        serializer = RoomListSerializer(all_room, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required.")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoice.EXPERIENCES:
                    raise ParseError("The category kind should be 'rooms'.")
            except Category.DoesNotExist:
                raise ParseError("Category is not found.")
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        created_room = serializer.save(
                            owner=request.user,
                            category=category,
                        )
                        amenities = request.data.get("amenity")
                        for amenity_pk in amenities:
                            # try:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            # except Amenity.DoesNotExist:
                            #     raise ParseError(f"Amenity with id {amenity_pk} is not found.")
                            created_room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(created_room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity is not found.")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)
