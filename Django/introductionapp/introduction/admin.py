from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from django import forms
from django.urls import path

from .models import Employer, Recruitment, User, Career,  Experience, Salary, Address, Tag, Profile, EducationProfile, \
    ExperienceProfile, University, CVOnline


class CareerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
    search_fields = ['number']
    list_filter = ['id', 'number']


class SalaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'salary']
    search_fields = ['salary']
    list_filter = ['id', 'salary']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_superuser',
                    'is_staff',
                    'is_active', 'date_joined']
    search_fields = ['username', 'email']
    list_filter = ['id', 'username', 'email', 'is_superuser', 'is_staff',
                   'is_active', 'date_joined']


class EmployerForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Employer
        fields = '__all__'


class EmployerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description', 'phone_number','address', 'recruiter']
    search_fields = ['name']
    list_filter = ['id', 'name', 'phone_number']
    form = EmployerForm


class CVOnlineAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'cv', 'profile']
    search_fields = ['title']


class RecruitmentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Recruitment
        fields = '__all__'


class RecruitmentAdmin(admin.ModelAdmin):
    form = RecruitmentForm


class ProfileForm(forms.ModelForm):
    skills = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm


class EducationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = EducationProfile
        fields = '__all__'


class EducationAdmin(admin.ModelAdmin):
    form = EducationForm


class ExperienceProfileForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = ExperienceProfile
        fields = '__all__'


class ExperienceProfileAdmin(admin.ModelAdmin):
    form = ExperienceProfileForm



admin.site.register(Employer, EmployerAdmin)
admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EducationProfile, EducationAdmin),
admin.site.register(ExperienceProfile, ExperienceProfileAdmin),
admin.site.register(University, UniversityAdmin),
admin.site.register(CVOnline, CVOnlineAdmin)