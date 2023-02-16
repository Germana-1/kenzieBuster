from rest_framework import serializers
from .models import RatingChoices, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices,
        default=RatingChoices.G,
    )
    synopsis = serializers.CharField(default=None)
    added_by = serializers.EmailField(read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj) -> int:
        return obj.movie.title

    def get_buyed_by(self, obj) -> int:
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
