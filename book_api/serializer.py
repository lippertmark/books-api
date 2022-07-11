from rest_framework import serializers
from book_api.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    number_of_pages = serializers.IntegerField()
    published_data = serializers.DateField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.published_data = validated_data.get('published_data', instance.published_data)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
