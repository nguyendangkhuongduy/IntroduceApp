# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Employer, Recruitment, User, Address, Experience, Salary, Career, Tag


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
    image = SerializerMethodField()

    def get_image(self, recruitment):
        requests = self.context['request']
        name = recruitment.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return requests.build_absolute_uri(path)

    class Meta:
        model = Employer
        fields = ["id", "name", "description", "email", "image", "created_date", "updated_date", "active"]


class RecruitmentSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, recruitment):
        requests = self.context['request']
        name = recruitment.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return requests.build_absolute_uri(path)

    class Meta:
        model = Recruitment
        fields = ["id", "content", "image", "title", "employer", "tags", "created_date", "updated_date", "active"]


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "avatar", "date_joined"]

        extra_kwargs = {
            'password': {'write_only': 'true'}
        }




