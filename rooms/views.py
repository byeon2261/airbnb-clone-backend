import time
from django.db import transaction
from django.conf import settings
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateRoomBookingSerializer
from categories.models import Category
from medias.serializers import PhotoSerializer
from reviews.serializers import ReviewSerializer
from reviews.models import Review


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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()

        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_room = Room.objects.all()
        serializer = RoomListSerializer(
            all_room,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = RoomDetailSerializer(
            data=request.data,
        )

        if serializer.is_valid():
            category_pk = request.data.get("category")

            if not category_pk:
                raise ParseError("Category is required.")
            try:
                category = Category.objects.get(pk=category_pk)

                if category.kind == Category.CategoryKindChoice.EXPERIENCES:
                    raise ParseError("The category kind should be 'rooms'.")

            except Category.DoesNotExist:
                raise ParseError("Category is not found.")
            try:
                with transaction.atomic():
                    created_room = serializer.save(
                        owner=request.user,
                        category=category,
                    )
                    amenities = request.data.get("amenities")

                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        created_room.amenities.add(amenity)

                    serializer = RoomDetailSerializer(
                        created_room,
                        context={"request": request},
                    )
                    return Response(serializer.data)
            except Exception as e:
                print(e)
                raise ParseError("Amenity is not found.")
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RoomDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)

        serializer = RoomDetailSerializer(
            room,
            context={"request": request},
        )

        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)

        if room.owner != request.user:
            raise PermissionDenied

        serializer = RoomDetailSerializer(
            room,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            category_pk = request.data.get("category")
            if category_pk:
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoice.EXPERIENCES:
                        raise ParseError("The category kind should be rooms.")
                except Category.DoesNotExist:
                    raise ParseError(detail="Category is not found.")

            try:
                with transaction.atomic():
                    if category_pk:
                        room = serializer.save(category=category)
                    else:
                        room = serializer.save()

                    amenities = request.data.get("amenities")
                    if amenities:
                        room.amenities.clear()
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                    serializer = RoomDetailSerializer(
                        room,
                        context={"request": request},
                    )
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Amenity is not found.")
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room = self.get_object(pk)

        if room.owner != request.user:
            raise PermissionDenied
        room.delete()

        return Response(status=HTTP_204_NO_CONTENT)


class RoomReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)

        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1

        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        reviews = room.reviews.all()
        serializer = ReviewSerializer(
            reviews[start:end],
            many=True,
        )

        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            created_review = serializer.save(
                user=request.user,
                room=self.get_object(pk),
            )
            serializer = ReviewSerializer(created_review)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RoomAmenities(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)

        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1

        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        amenities = room.amenities.all()
        serializer = AmenitySerializer(
            amenities[start:end],
            many=True,
        )

        return Response(serializer.data)


class RoomPhotos(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)

        if request.user != room.owner:
            raise PermissionDenied

        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            created_photo = serializer.save(room=room)
            serializer = PhotoSerializer(created_photo)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RoomBookings(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        # now = timezone.localtime(timezone.now()).date()
        now = timezone.localtime().date()  # 오류X. 오류 발생시 변경

        bookings = Booking.objects.filter(
            room=room,
            kind=Booking.BookingKindChoice.ROOM,
            check_in__gt=now,
        )
        serializer = PublicBookingSerializer(
            bookings,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request, pk):
        room = self.get_object(pk)
        serializer = CreateRoomBookingSerializer(data=request.data)

        if serializer.is_valid():
            saved_booking = serializer.save(
                kind=Booking.BookingKindChoice.ROOM,
                user=request.user,
                room=room,
            )
            serializer = PublicBookingSerializer(saved_booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
