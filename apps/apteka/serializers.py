from rest_framework import serializers
from .models import Pill, Type, Doctor, Rating, Partner, Achievement, Category


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = [
            'id',
            'name'
        ]


class PillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pill
        fields = [
            'id', 'name', 'body', 'price', 'information', 'type',
            'expiration_date', 'usage_url', 'picture', 'discount_price',
            'published', 'created_at', 'updated_at'
        ]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'direction', 'call', 'body', 'picture',
                  'tavsiflari_dori', 'published'
                  ]


class RatingSerializer(serializers.ModelSerializer):
    pill = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'rank', 'pill']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'image']


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'image', 'title', 'description']


class CategorySerializer(serializers.ModelSerializer):
    pills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'pills']
