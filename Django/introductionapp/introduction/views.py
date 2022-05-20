import profile

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
    , Rating, Comment, ViewEmployer, Profile, University, ExperienceProfile, EducationProfile, CVOnline
from .serializers import EmployerSerializer, RecruitmentSerializer, UserSerializer, CareerSerializer, \
    SalarySerializer, ExperienceSerializer, TagSerializer,\
    AddressSerializer, ActionSerializer, RatingSerializer, CommentSerializer,  ViewEmployerSerializer,\
    ProfileSerializer, EmployerDetailsSerializer, EducationProfileSerializer, ExperienceProfileSerializer, CVOnlineSerializer
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


class TagViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EmployerViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Employer.objects.filter(active=True)
    serializer_class = EmployerSerializer

    def get_permissions(self):
        if self.action in ['add-comment', 'rating', 'like']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        employer = self.queryset

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
        return Response(RecruitmentSerializer(recruitment, context={'request': request}, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='add_recruitment')
    def add_recruitment(self, request, pk):
        content = request.data.get('content')
        employ = Employer.objects.get(pk=pk)
        recruitment = employ.recruitment.filter(active=True)
        return Response(RecruitmentSerializer(recruitment, context={'request': request}, many=True).data,
                        status=status.HTTP_200_OK)

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

    @action(methods=['get'], detail=True, url_path='view')
    def inc_view(self, request, pk):
        v, created = ViewEmployer.objects.get_or_create(employer=self.get_object())
        v.view = F('view') + 1
        v.save()

        v.refresh_from_db()

        return Response(ViewEmployerSerializer(v).data, status=status.HTTP_200_OK)


# API lấy tất cả các tin tuyển dụng
# API đăng ký người dùng
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['get_profile', 'cv']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @get_current_user.mapping.patch
    def update_user(self, request):
        user = request.user
        data = request.data

        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        email = data.get('email')

        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name

        if username:
            user.username = username

        if password:
            user.set_password(password)

        if email:
            user.email = email

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
        pro = Profile.objects.filter(user=self.get_object()).first()
        return Response(data=ProfileSerializer(pro, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @get_job_profile.mapping.patch
    def update_profile(self, request, pk):
        # pro = Profile.objects.filter(user=User.objects.get(pk=pk)).first()
        # pro = request.pro
        pro = Profile.objects.filter(user=self.get_object()).first()
        data = request.data

        full_name = data.get('full_name')
        phone_number = data.get('phone_number')
        gender = data.get('gender')
        date_of_birth = data.get('date_of_birth')
        address_detail = data.get('address_detail')
        skills = data.get('skills')

        if full_name:
            pro.full_name = full_name

        if phone_number:
            pro.phone_number = phone_number

        if gender:
            pro.gender = gender

        if date_of_birth:
            pro.date_of_birth = date_of_birth

        if address_detail:
            pro.address_details = address_detail

        if skills:
            pro.skills = skills

        try:
            pro.save()
        except():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=ProfileSerializer(pro, context={'request': request}).data,
                            status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True,
            url_path='company')
    def get_company(self, request, pk):
        company = Employer.objects.filter(recruiter=self.get_object()).first()
        return Response(data=EmployerSerializer(company, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    # @get_company.mapping.post
    # def create_or_update_company(self, request, pk):
    #     company = Employer.objects.filter(recruiter=self.get_object()).first()
    #     stt = None
    #     data = request.data
    #     data['recruitment'] = self.get_object().id
    #     if company:
    #         # update
    #         serializer = EmployerSerializer(company, data=data, partial=True)
    #         stt = status.HTTP_200_OK
    #     else:
    #         # create
    #         serializer = EmployerSerializer(data=data)
    #         stt = status.HTTP_201_CREATED
    #     if serializer.is_valid(raise_exception=True):
    #         # save
    #         serializer.save()
    #         return Response(data=serializer.data, status=stt)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True,
            url_path='cv')
    def get_cv(self, request, pk):
        company = CVOnline.objects.filter(user=self.get_object()).first()
        return Response(data=CVOnlineSerializer(company, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @get_cv.mapping.post
    def update_cv(self, request, pk):
        company = CVOnline.objects.filter(user=self.get_object()).first()
        data = request.data

        cv = data.get('cv')
        title = data.get('title')

        if cv:
            company.cv = cv

        if title:
            company.title = title

        try:
            company.save()
        except():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=ProfileSerializer(company, context={'request': request}).data,
                            status=status.HTTP_200_OK)


class RecruitmentViewSet(viewsets.ViewSet, generics.ListAPIView,
                         generics.RetrieveAPIView,
                         generics.CreateAPIView,
                         generics.UpdateAPIView, generics.DestroyAPIView):
    pagination_class = BasePagination
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = self.queryset

        q = self.request.query_params.get('q')
        if q is not None:
            queryset = Recruitment.objects.filter(title__icontains=q)

        career_id = self.request.query_params.get('career_id')
        if career_id:
            queryset = queryset.filter(career_id=career_id)

        recruitment_id = self.request.query_params.get('recruitment_id')
        if recruitment_id:
            queryset = queryset.filter(recruitment_id=recruitment_id)

        salary_id = self.request.query_params.get('salary_id')
        if salary_id:
            queryset = self.objects.filter('salary_id')

        experience_id = self.request.query_params.get('experience_id')
        if experience_id:
            queryset = queryset.filter(experience_id=experience_id)
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
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super().destroy(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class ProfileViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action in ['experience', 'education']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=True, url_path='experience')
    def get_experience(self, request, pk):
        experience = ExperienceProfile.objects.filter(profile=self.get_object()).first()
        return Response(data=ExperienceProfileSerializer(experience,
                                                         context={'request': request}).data, status=status.HTTP_200_OK)

    @get_experience.mapping.patch
    def update_experience(self, request, pk):
        experience = ExperienceProfile.objects.filter(profile=self.get_object()).first()
        data = request.data

        job = data.get('job')
        position = data.get('position')
        time_start = data.get('time_start')
        time_end = data.get('time_end')
        company_name = data.get('company_name')
        description = data.get('description')

        if job:
            experience.job = job

        if position:
            experience.position = position

        if time_start:
            experience.time_start = time_start

        if time_end:
            experience.time_end = time_end

        if company_name:
            experience.company_name = company_name

        if description:
            experience.description = description

        try:
            experience.save()
        except():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=self.serializer_class(experience, context={'request': request}).data,
                            status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='education')
    def get_education(self, request, pk):
        edu = EducationProfile.objects.filter(profile=self.get_object()).first()
        return Response(data=EducationProfileSerializer(edu,
                                                        context={'request': request}).data, status=status.HTTP_200_OK)

    @get_education.mapping.patch
    def update_education(self, request, pk):
        edu = EducationProfile.objects.filter(profile=self.get_object()).first()
        data = request.data

        degree = data.get('degree')
        major = data.get('major')
        time_start = data.get('time_start')
        time_completed = data.get('time_completed')
        description = data.get('description')

        if degree:
            edu.degree = degree

        if major:
            edu.major = major

        if time_start:
            edu.time_start = time_start

        if time_completed:
            edu.time_completed = time_completed

        if description:
            edu.description = description

        try:
            edu.save()
        except():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=self.serializer_class(edu, context={'request': request}).data,
                            status=status.HTTP_200_OK)





