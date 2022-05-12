from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions, mixins
from rest_framework.decorators import action, permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
# from .paginators import CoursePaginator
from drf_yasg.utils import swagger_auto_schema
# from .perms import CommentOwnerPerms
from rest_framework.views import APIView

from .models import Employer, Recruitment, User, Career, Salary, Experience, Address, Tag, Action, Rating, Comment, ViewEmployer
from .serializers import EmployerSerializer, RecruitmentSerializer, UserSerializer, CareerSerializer, \
    SalarySerializer, ExperienceSerializer, TagSerializer,\
    AddressSerializer, ActionSerializer, RatingSerializer, CommentSerializer,  ViewEmployerSerializer
from .paginator import BasePagination
from django.conf import settings

from django.db.models import F


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

    def get_permissions(self):
        if self.action in ['like', 'rating', 'add-comment', 'get-comment']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    def get_queryset(self):
        employer = Employer.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            employer = Employer.objects.filter(name__icontains=q)

        e_id = self.request.query_params.get('id')
        if e_id is not None:
            employer = Employer.objects.filter(id=e_id)

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
class RecruitmentViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
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
    parser_classes = [MultiPartParser, ]

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


class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super().destroy(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


