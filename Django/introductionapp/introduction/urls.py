from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("employer", views.EmployerViewSet, 'employer')
router.register("recruitment", views.RecruitmentViewSet, 'recruitment')
router.register("users", views.UserViewSet, 'users')
router.register("salary", views.SalaryViewSet, 'salary')
router.register("address", views.AddressViewSet, 'address')
router.register("experience", views.ExperienceViewSet, 'experience')
router.register("career", views.CareerViewSet, 'career')
router.register("tag", views.TagViewSet, 'tag')
router.register("comments", views.CommentViewSet, 'comment')
router.register("profile", views.ProfileViewSet, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view())
]