# from rest_framework import serializers
# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Employer, Recruitment, User, Address, Experience, Salary, Career, Tag, Action, Rating,\
    ViewEmployer, ViewProfile, Profile, University, EducationProfile, CVOnline, Comment, ExperienceProfile
from django.contrib.auth.models import Group
from . import perms


# class EmployerPermSerializer(ModelSerializer):
#     # class Meta:
#     #     model = User
#     #     fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
#     #     extra_kwargs = {
#     #         'password': {
#     #             'write_only': True
#     #         }, 'avatar': {
#     #             'write_only': True
#     #         }
#     #     }
#     class Meta:
#         model = User
#         fields = ["id", "first_name", "last_name", "username", "groups", "password", "email", "avatar", "date_joined"]
#
#         extra_kwargs = {
#             'password': {'write_only': 'true'}
#         }
#
#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(user.password)
#         user.Is_Employer = True
#         group = Group.objects.get(pk=2)
#         user.save()
#         user.groups.add(group)
#         employer = Employer(user=user)
#         employer.save()
#         return user


# Action
class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "created_date"]


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rating", "created_date"]


class UserSerializer(ModelSerializer):

    avatar = SerializerMethodField()

    def get_avatar(self, obj):
        request = self.context.get('request')
        name = obj.avatar.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        if request:
            return request.build_absolute_uri(path)
        else:
            return None

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "avatar", "date_joined", "Role"]

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
    image = SerializerMethodField()

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
        fields = ["id", "name", "address", "description", "phone_number",
                  "email", "image", "created_date", "active"]


class EmployerDetailsSerializer(EmployerSerializer):
    rating = SerializerMethodField()

    def get_rater(self, employer):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            r = employer.employer_rater.filter(recruiter=request.user).first()
            if r:
                return r.rating
        return -1

    class Meta:
        model = EmployerSerializer.Meta.model
        fields = EmployerSerializer.Meta.fields + ['rating']


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
    user = UserSerializer()
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = "__all__"


class ExperienceProfileSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = ExperienceProfile
        fields = "__all__"


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University()
        fields = "__all__"


class EducationProfileSerializer(ModelSerializer):
    profile = ProfileSerializer()
    university_name = UniversitySerializer()

    class Meta:
        model = EducationProfile
        fields = "__all__"


class CVOnlineSerializer(ModelSerializer):
    cv = SerializerMethodField()
    profile = ProfileSerializer()
    user = UserSerializer()

    def get_cv(self, vv):
        request = self.context.get("request")
        name = vv.cv.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        if request:
            return request.build_absolute_uri(path)
        else:
            return None

    class Meta:
        model = CVOnline
        fields = "__all__"










