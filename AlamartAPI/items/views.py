from .models import Item
from .serializers import ItemSerializers
from rest_framework import status, generics, views


class ItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
