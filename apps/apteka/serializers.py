from rest_framework import serializers
from .models import Pill, Type, Doctor, Rating, Partner, Achievement, Category


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = [
            'id',
            'name_uz',
            'name_ru',
            'name_en',
        ]


class PillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pill
        fields = [
            'id', 'name_uz', 'name_ru', 'name_en',
            'body_uz', 'body_ru', 'body_en',
            'price',
            'information_uz', 'information_ru', 'information_en',
            'type_uz', 'type_ru', 'type_uz',
            'expiration_date', 'usage_url', 'picture', 'discount_price',
            'published', 'created_at', 'updated_at',
        ]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'direction_uz', 'direction_ru', 'direction_en',
                  'call', 'body_uz', 'body_ru', 'body_en',
                  'picture', 'advices'
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
        fields = ['id', 'image', 'title_uz', 'title_ru', 'title_en',
                  'description_uz', 'description_ru', 'description_en',
                  ]


class CategorySerializer(serializers.ModelSerializer):
    pills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'name_en', ]
