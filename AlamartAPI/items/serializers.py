
from rest_framework import serializers

from AlamartAPI.items.models import Item


class ItemSerializers(serializers.ModelSerializer):

    maker = serializers.CharField(source='maker.name', read_only=True)
    availability = serializers.BooleanField(source='is_available', read_only=True)

    class Meta:
        model = Item
        exclude = ('id', 'sold', 'stock')
