from django.db import models


class Maker(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    size = models.IntegerField()
    stock = models.IntegerField(default=0)
    sold = models.IntegerField()
    maker = models.ForeignKey(to=Maker, related_name='rel_maker', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        if self.stock > 0:
            return True
        return False;

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


class ItemImages(models.Model):
    imageURL = models.CharField(max_length=100)
    item = models.ForeignKey(to=Item, related_name='rel_images', on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name
