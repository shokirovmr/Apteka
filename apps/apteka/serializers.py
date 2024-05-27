from typing import List

from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Pill, Type, Doctor, Partner, Achievement, Category, Commentary, Entry


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
    categories_uz = serializers.SerializerMethodField('get_categories_uz')
    categories_ru = serializers.SerializerMethodField('get_categories_ru')
    categories_en = serializers.SerializerMethodField('get_categories_en')
    type_uz = serializers.SerializerMethodField('get_type_uz')
    type_ru = serializers.SerializerMethodField('get_type_ru')
    type_en = serializers.SerializerMethodField('get_type_en')

    class Meta:
        model = Pill
        fields = [
            'id', 'categories_uz', 'categories_ru', 'categories_en',
            'name_uz', 'name_ru', 'name_en',
            'body_uz', 'body_ru', 'body_en',
            'price',
            'information_uz', 'information_ru', 'information_en',
            'type_uz', 'type_ru', 'type_en',
            'expiration_date', 'usage_url', 'picture', 'discount_price',
            'published', 'created_at', 'updated_at',
        ]

    def get_categories_uz(self, obj) -> list[str]:
        categories = obj.categories.all()
        return [obj.name_uz for obj in categories]

    def get_categories_ru(self, obj) -> list[str]:
        categories = obj.categories.all()
        return [obj.name_ru for obj in categories]

    def get_categories_en(self, obj) -> list[str]:
        categories = obj.categories.all()
        return [obj.name_en for obj in categories]

    def get_type_uz(self, obj) -> str:
        type_name = obj.type.name
        return type_name

    def get_type_ru(self, obj) -> str:
        type_name = obj.type.name_ru
        return type_name

    def get_type_en(self, obj) -> str:
        type_name = obj.type.name_en
        return type_name


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'direction_uz', 'direction_ru', 'direction_en',
                  'call', 'body_uz', 'body_ru', 'body_en',
                  'picture', 'advices'
                  ]


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
    pills = serializers.SerializerMethodField('get_pills')

    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'pills']

    @extend_schema_field(List[dict])
    def get_pills(self, obj) -> List[dict]:
        pills = obj.pills.all()
        return PillSerializer(pills, many=True).data


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ['id', 'author', 'body', 'published']


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'fullname', 'phonenumber', 'created_at']


class DiscountPillSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField("get_percentage", read_only=True)

    class Meta:
        model = Pill
        fields = [
            'id', 'name_uz', 'name_ru', 'name_en',
            'body_uz', 'body_ru', 'body_en',
            'price', 'percentage',
            'information_uz', 'information_ru', 'information_en',
            'type',
            'expiration_date', 'usage_url', 'picture', 'discount_price',
            'published', 'created_at', 'updated_at',
        ]

    def get_percentage(self, obj) -> float:
        return (obj.price - obj.discount_price) / obj.price * 100


class SmallPillSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField("get_price")

    class Meta:
        model = Pill
        fields = [
            'id', 'name_uz', 'name_ru', 'name_en', 'picture', 'price', 'rank'
        ]

    def get_price(self, object) -> float:
        if object.discount_price:
            return object.discount_price
        else:
            return object.price
