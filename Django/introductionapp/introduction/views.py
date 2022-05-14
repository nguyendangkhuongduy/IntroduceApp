from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions, mixins
from rest_framework.decorators import action, permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
# from .paginators import CoursePaginator
from drf_yasg.utils import swagger_auto_schema
# from .perms import CommentOwnerPerms
from rest_framework.views import APIView

from .models import Employer, Recruitment, User, Career, Salary, Experience, Address, Tag, Action\
    , Rating, Comment, ViewEmployer, Profile
from .serializers import EmployerSerializer, RecruitmentSerializer, UserSerializer, CareerSerializer, \
    SalarySerializer, ExperienceSerializer, TagSerializer,\
    AddressSerializer, ActionSerializer, RatingSerializer, CommentSerializer,  ViewEmployerSerializer,\
    ProfileSerializer
from .paginator import BasePagination
from django.conf import settings

from django.db.models import F

from . import perms


# API lấy danh sách các nhà tuyển dụng
# API lấy các tin tuyển dụng từ nhà tuyển dụng

class CareerViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class ExperienceViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SalaryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class AddressViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # @action(methods=['get'], detail=True, url_path='address')
    # def get_address(self, request, pk):
    #     districts = Address.objects.filter(city=self.get_object()).all()
    #     return Response(data=AddressSerializer(districts, many=True, ).data, status=status.HTTP_200_OK)


class TagViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EmployerViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Employer.objects.filter(active=True)
    serializer_class = EmployerSerializer

    # def get_permissions(self):
    #     if self.action in ['like', 'rating', 'add-comment', 'get-comment']:
    #         return [permissions.IsAuthenticated()]
    #
    #     return [permissions.AllowAny()]
    def get_permissions(self):
        if self.action in ['add_comment', 'rating', 'like']:
            return [perms.IsRecruiterUserUser()]
        elif self.action in ['view']:
            return [perms.IsEmployerUserUser()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        employer = Employer.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            employer = Employer.objects.filter(name__icontains=q)

        e_id = self.request.query_params.get('id')
        if e_id is not None:
            employer = Employer.objects.filter(id=e_id)

        kw = self.request.query_params.get('kw')
        if kw:
            employer = employer.filter(name__icontains=kw)

        return employer

    @action(methods=['get'], detail=True, url_path='recruitment')
    def get_recruitment(self, request, pk):
        employ = Employer.objects.get(pk=pk)
        recruitment = employ.recruitment.filter(active=True)
        return Response(RecruitmentSerializer(recruitment, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='like')
    def take_like(self, request, pk):
        try:
            action_type = int(request.data.get('type'))
        except IndexError | ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Action.objects.create(type=action_type, user=request.user, employer=self.get_object())

            return Response(ActionSerializer(action).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='rating')
    def take_rate(self, request, pk):
        try:
            rating = int(request.data.get('rating'))
        except IndexError | ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            r = Rating.objects.create(rating=rating, user=request.user, employer=self.get_object())

            return Response(RatingSerializer(r).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="add-comment")
    def add_comment(self, request, pk):
        content = request.data.get('content')
        if content:
            c = Comment.objects.create(content=content, company=self.get_object(), user=request.user)
            return Response(CommentSerializer(c).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True, url_path='get-comment')
    def get_comments(self, request, pk):
        company = self.get_object()
        comments = company.comments.filter(active=True)

        return Response(data=CommentSerializer(comments, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)
        # company = self.get_object()
        # comments = company.comments.select_related('user').filter(active=True)
        #
        # return Response(CommentSerializer(comments, many=True).data,
        #                 status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='view')
    def inc_view(self, request, pk):
        v, created = ViewEmployer.objects.get_or_create(employer=self.get_object())
        v.view = F('view') + 1
        v.save()

        v.refresh_from_db()

        return Response(ViewEmployerSerializer(v).data, status=status.HTTP_200_OK)


# API lấy tất cả các tin tuyển dụng
# API đăng ký người dùng
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['get_profile']:
            return [perms.IsRecruiterUser()]
        return [permissions.AllowAny()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.data.get('groups')[0].get('name') not in [perms.IsEmployerUser, perms.recruiter_role]:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)

    @get_current_user.mapping.patch
    def update_user(self, request):
        user = request.user
        data = request.data

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        email_notification_active = data.get('email_notification_active')

        if username:
            user.username = username

        if password:
            user.set_password(password)

        if email:
            user.email = email

        if email_notification_active:
            user.email_notification_active = bool(email_notification_active)

        try:
            user.save()
        except():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=self.serializer_class(user, context={'request': request}).data,
                            status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True,
            url_path='profile', url_name='get_profile')
    def get_job_profile(self, request, pk):
        profile = Profile.objects.filter(user=self.get_object()).first()
        return Response(data=ProfileSerializer(profile, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @get_job_profile.mapping.post
    def create_update_job_profile(self, request, pk):
        profile = Profile.objects.filter(job_seeker=self.get_object()).first()
        stt = None

        if profile:
            # update
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            stt = status.HTTP_200_OK
        else:
            # create
            serializer = ProfileSerializer(data=request.data)
            stt = status.HTTP_201_CREATED
        if serializer.is_valid(raise_exception=True):
            # save
            serializer.save()
            return Response(data=serializer.data, status=stt)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True,
            url_path='company', url_name='get_company')
    def get_company(self, request, pk):
        company = Employer.objects.filter(recruiter=self.get_object()).first()
        return Response(data=EmployerSerializer(company, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @get_company.mapping.post
    def create_or_update_company(self, request, pk):
        company = Employer.objects.filter(recruiter=self.get_object()).first()
        stt = None
        data = request.data
        data['recruitment'] = self.get_object().id
        if company:
            # update
            serializer = EmployerSerializer(company, data=data, partial=True)
            stt = status.HTTP_200_OK
        else:
            # create
            serializer = EmployerSerializer(data=data)
            stt = status.HTTP_201_CREATED
        if serializer.is_valid(raise_exception=True):
            # save
            serializer.save()
            return Response(data=serializer.data, status=stt)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruitmentViewSet(viewsets.ViewSet, generics.ListAPIView,
                         generics.RetrieveAPIView,
                         generics.CreateAPIView,
                         generics.UpdateAPIView):
    pagination_class = BasePagination
    serializer_class = RecruitmentSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [perms.JobPostOwnerPerms()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = self.queryset

        career_id = self.request.query_params.get('career_id')
        if career_id:
            queryset = queryset.filter(career_id=career_id)

        recruitment_id = self.request.query_params.get('recruitment_id')
        if recruitment_id:
            queryset = queryset.filter(recruitment_id=recruitment_id)

        salary_id = self.request.query_params.get('salary_id')
        if salary_id:
            queryset = queryset.filter(salary_id=salary_id)

        experience_id = self.request.query_params.get('experience_id')
        if experience_id:
            queryset = queryset.filter(experience_id=experience_id)

        kw = self.request.query_params.get('kw')
        if kw:
            queryset = queryset.filter(title__icontains=kw)

        return queryset


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [perms.IsRecruiterUser()]
        return [permissions.IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super().destroy(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


