from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
# from .paginators import CoursePaginator
from drf_yasg.utils import swagger_auto_schema
# from .perms import CommentOwnerPerms
from rest_framework.views import APIView

from .models import Employer, Recruitment, User, Career, Salary, Experience, Address, Tag
from .serializers import EmployerSerializer, RecruitmentSerializer, UserSerializer, CareerSerializer, \
    SalarySerializer, ExperienceSerializer, TagSerializer\
    , AddressSerializer
from .paginator import BasePagination
from django.conf import settings


# API lấy danh sách các nhà tuyển dụng
# API lấy các tin tuyển dụng từ nhà tuyển dụng

class CareerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class ExperienceViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SalaryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class AddressViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class TagViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EmployerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Employer.objects.filter(active=True)
    serializer_class = EmployerSerializer

    def get_queryset(self):
        employer = Employer.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            employer = Employer.objects.filter(name__icontains=q)

        e_id = self.request.query_params.get('id')
        if e_id is not None:
            employer = Employer.objects.filter(id=e_id)

        return employer

    @action(methods=['get'], detail=True, url_path='recruitments')
    def get_recruitment(self, request, pk):
        # employ = Employer.objects.get(pk=pk)
        recruitments = self.get_object().recruitment.filter(active=True)
        return Response(RecruitmentSerializer(recruitments, many=True).data, status=status.HTTP_200_OK)


# API lấy tất cả các tin tuyển dụng
class RecruitmentViewSet(viewsets.ViewSet, generics.ListAPIView):
    pagination_class = BasePagination
    serializer_class = RecruitmentSerializer

    def get_queryset(self):
        recruitment = Recruitment.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            recruitment = Recruitment.objects.filter(title__icontains=q)

        employ_id = self.request.query_params.get('employer_id')
        if employ_id is not None:
            recruitment = Recruitment.objects.filter(employer_id=employ_id)

        return recruitment


# API đăng ký người dùng
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)


