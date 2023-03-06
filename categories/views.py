from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewset(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRoomViewset(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(kind=Category.CategoryKindChoice.ROOMS)
