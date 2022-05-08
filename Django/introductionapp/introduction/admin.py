from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from django import forms
from django.urls import path

from .models import Employer, Recruitment, User, Career,  Experience, Salary, Address, Tag


class CareerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
    search_fields = ['number']
    list_filter = ['id', 'number']


class SalaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'salary']
    list_display_links = ['salary']
    search_fields = ['salary']
    list_filter = ['id', 'salary']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    list_display_links = ['address']
    search_fields = ['address']
    list_filter = ['id', 'address']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_superuser',
                    'is_staff',
                    'is_active', 'date_joined']
    list_display_links = ['username']
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
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['id', 'name', 'phone_number']
    form = EmployerForm


class RecruitmentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Recruitment
        fields = '__all__'


class RecruitmentAdmin(admin.ModelAdmin):
    form = RecruitmentForm


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Career, CareerAdmin)
