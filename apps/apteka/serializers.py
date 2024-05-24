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
    categories = serializers.SerializerMethodField('get_categories')

    class Meta:
        model = Pill
        fields = [
            'id', 'categories', 'name_uz', 'name_ru', 'name_en',
            'body_uz', 'body_ru', 'body_en',
            'price',
            'information_uz', 'information_ru', 'information_en',
            'type_uz', 'type_ru', 'type_uz',
            'expiration_date', 'usage_url', 'picture', 'discount_price',
            'published', 'created_at', 'updated_at',
        ]

    def get_categories(self, obj):
        categories = obj.categories.all()
        return map(lambda obj: obj.name, categories)


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
    pills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'pills', ]


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ['id', 'author', 'body', 'published']


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'fullname', 'phonenumber', 'created_at']


class DiscountPillSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField("get_percentage")

    class Meta:
        model = Pill
        fields = [
            'id', 'name_uz', 'name_ru', 'name_en',
            'body_uz', 'body_ru', 'body_en',
            'price', 'percentage',
            'information_uz', 'information_ru', 'information_en',
            'type_uz', 'type_ru', 'type_uz',
            'expiration_date', 'usage_url', 'picture', 'discount_price',
            'published', 'created_at', 'updated_at',
        ]

    def get_percentage(self, object):
        return (object.price - object.discount_price) / object.price * 100


class SmallPillSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField("get_price")

    class Meta:
        model = Pill
        fields = [
            'id', 'name_uz', 'name_ru', 'name_en', 'picture', 'price', 'rank'
        ]

    def get_price(self, object):
        if object.discount_price:
            return object.discount_price
        else:
            return object.price
