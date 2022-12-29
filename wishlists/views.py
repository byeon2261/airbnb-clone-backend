from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Wishlist
from rooms.models import Room
from .serializers import WishlistSerializer


class WishLists(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(
            all_wishlists,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)

        if serializer.is_valid():
            created_wishlist = serializer.save(user=request.user)
            serializer = WishlistSerializer(created_wishlist)

            return Response(serializer.data)
        else:
            Response(serializer.errors)
