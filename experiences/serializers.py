from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Perk, Experience
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"

class ExperienceListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "id",
            "pk",
            "name",
            "country",
            "city",
            "host",
            "price",
            "perks",
            "address",
            "start",
            "end",
            "description",
            "rating",
            "is_host",
            "category",
        )
    
    def get_rating(self, experience):
        return experience.rating()
    
    def get_is_host(self, experience):
        request = self.context['request']
        return experience.host == request.user

class ExperienceDetailSerializer(ModelSerializer):

    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )
    reviews = ReviewSerializer(
        read_only=True,
        many=True,
    )
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "pk",
            "name",
            "description",
            "country",
            "city",
            "address",
            "rating",
            "price",
            "is_liked",
            "start",
            "end",
            "is_host",
            "host",
            "category",
            "perks",
            "reviews",
            "created_at",
            "updated_at",
        )

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user

    def get_is_liked(self, experience):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user=request.user,
            experiences__pk=experience.pk,
        ).exists()