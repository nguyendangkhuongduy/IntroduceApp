# from rest_framework import serializers
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Employer, Recruitment, User, Address, Experience, Salary, Career, Tag, Action, Rating,\
    ViewEmployer, ViewProfile, Profile, University, EducationProfile, ExperienceProfile, CVOnline, Comment


# Action
class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "created_date"]


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rating", "created_date"]


# class UserSerializer(ModelSerializer):
    # avatar = SerializerMethodField(source='avatar')
    #
    # def get_avatar(self, obj):
    #     request = self.context['request']
    #     if obj.avatar and not obj.avatar.name.startswith("/static"):
    #         path = '/static/%s' % obj.avatar.name
    #
    #         return request.build_absolute_uri(path)

    # class Meta:
    #     model = User
    #     fields = ['id', 'first_name', 'last_name',
    #               'username', 'password', 'email']
    #     extra_kwargs = {
    #         'password': {
    #             'write_only': True
    #         }
    #     }

    # def create(self, validated_data):
    #     data = validated_data.copy()
    #     user = User(**data)
    #     user.set_password(user.password)
    #     user.save()
    #
    #     return user
class UserSerializer(serializers.ModelSerializer):
    def get_avatar(self, obj):
        request = self.context['request']
        if obj.avatar and not obj.avatar.name.startswith("/static"):
            path = '/static/%s' % obj.avatar.name

            return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "avatar", "date_joined"]

        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user


class CommentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ["id", "content", "user", "created_date", "updated_date"]


class ViewEmployerSerializer(ModelSerializer):
    class Meta:
        model = ViewEmployer
        fields = ['id', 'view']


class ViewProfileSerializer(ModelSerializer):
    class Meta:
        model = ViewProfile
        fields = ['id', 'view']


# Tim kiem
class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class SalarySerializer(ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"


class CareerSerializer(ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class EmployerSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    address = AddressSerializer()

    def get_image(self, recruitment):
        request = self.context.get('request')
        name = recruitment.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        if request:
            return request.build_absolute_uri(path)
        else:
            return None

    class Meta:
        model = Employer
        fields = ["id", "name", "address", "description", "phone_number", "email", "image", "created_date", "active"]


class EmployerDetailsSerializer(EmployerSerializer):
    class Meta:
        model = EmployerSerializer.Meta.model
        fields = EmployerSerializer.Meta.fields


class RecruitmentSerializer(ModelSerializer):
    image = SerializerMethodField()

    tags = TagSerializer(many=True)

    employer = EmployerSerializer()

    salary = SalarySerializer()

    address = AddressSerializer()

    career = CareerSerializer()

    experience = ExperienceSerializer()

    def get_image(self, recruitment):
        request = self.context.get("request")
        name = recruitment.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        if request:
            return request.build_absolute_uri(path)
        else:
            return None

    class Meta:
        model = Recruitment
        fields = "__all__"


# Ung vien
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class EducationProfileSerializer(ModelSerializer):
    class Meta:
        module = EducationProfile
        fields = "__all__"


