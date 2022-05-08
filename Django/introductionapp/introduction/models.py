from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')

    def __str__(self):
        return self.username


class ItemBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# class CVOnline(ItemBase):
#     # intro = RichTextField()
#     from_salary = models.DecimalField(default=0, decimal_places=2, max_digits=10)
#     to_salary = models.DecimalField(default=0, decimal_places=2, max_digits=10)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Address(models.Model):
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.address


class Salary(models.Model):
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.salary


class Career(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Experience(models.Model):
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number


class Employer(ItemBase):
    name = models.CharField(max_length=100, null=False, unique=True)
    description = RichTextField()
    phone_number = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, upload_to='employer/%Y/%m')
    recruiter = models.OneToOneField('User', on_delete=models.CASCADE, related_name='employer')
    commenter = models.ManyToManyField('User', through='Comment', related_name='employer_comment')
    rater = models.ManyToManyField('User', through='Rating',  related_name='employer_rating')

    def __str__(self):
        return self.name


# tin tuyen dung
class Recruitment(ItemBase):
    class Meta:
        ordering = ["-created_date"]

    # content = models.CharField(max_length=200, null=False)
    content = RichTextField()
    title = models.CharField(max_length=100, null=False)
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to='recruitment/%Y/%m')
    employer = models.ForeignKey(Employer, related_name='recruitment', on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.SET_NULL, null=True,
                               related_name='recruitment')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='recruitment')
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True, related_name='recruitment')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL,
                                   null=True, related_name='recruitment')
    tags = models.ManyToManyField('Tag', related_name='recruitment', blank=True)

    class Meta:
        ordering = ['-created_date', '-updated_date']


# Hồ sơ của ứng viên
class Profile(ItemBase):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=100)
    skills = RichTextField(null=True, blank=True)

    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#
# # tieu chi ung tuyen
# class Criteria(models.Model):
#     name = models.CharField(max_length=200,  null=False)
#     description = models.CharField(blank=True, null=True)
#     recruitment = models.ManyToManyField('Recruitment', on_delete=models.CASCADE)
#
#
# # Don ung tuyen
# class Form(ItemBase):
#     description = models.CharField(blank=True, null=True)
#     curriculum_vitae = models.FileField(upload_to='uploads/%y/%m')
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#
#
# # Nop don ung tuyen
# class ApplyForm(models.Model):
#     date = models.DateField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ActionBase(ItemBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Like(ActionBase):
    active = models.BooleanField(default=False)


class Rating(ItemBase):
    rating = models.SmallIntegerField(default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='ratings')


class Comment(ItemBase):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    company = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

