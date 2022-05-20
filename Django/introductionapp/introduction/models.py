from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


#1: ung vien
#2: nha tuyen dung
class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')
    Role = models.CharField(max_length=5, default=1)

    def __str__(self):
        return self.username


class ItemBase(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Address(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


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


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employer(ItemBase):
    name = models.CharField(max_length=100, null=False, unique=True)
    description = RichTextField(null=True)
    phone_number = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    address_details = models.CharField(max_length=100, null=False, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='employer')
    image = models.ImageField(null=True, upload_to='employer/%Y/%m')

    recruiter = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    commenter = models.ManyToManyField(User, through='Comment', related_name='employer_comment')
    rater = models.ManyToManyField(User, through='Rating',  related_name='employer_rating')

    def __str__(self):
        return self.name


# tin tuyen dung
class Recruitment(ItemBase):
    content = RichTextField()
    title = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=100, default=1)
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to='recruitment/%Y/%m')

    employer = models.ForeignKey(Employer, related_name='recruitment', on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.SET_NULL, null=True, related_name='recruitment')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='recruitment')
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True, related_name='recruitment')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True, related_name='recruitment')
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created_date', '-updated_date']

    def __str__(self):
        return self.title


class ActionBase(ItemBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Action(ActionBase):
    LIKE, DISLIKE = range(2)
    ACTIONS = [
        (LIKE, 'like'),
        (DISLIKE, 'dislike')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


class Like(ActionBase):
    active = models.BooleanField(default=False)


class Rating(ActionBase):
    rating = models.SmallIntegerField(default=5)


# Comment
class Comment(ItemBase):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    company = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.content


# Ung  vien
# Hồ sơ của ứng viên
class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    address_details = models.CharField(max_length=100, blank=True, null=True)
    skills = RichTextField(null=True, blank=True)

    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.full_name


class University(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


# Trinh do cua ung vien
class EducationProfile(models.Model):
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    time_start = models.DateField()
    time_completed = models.DateField()
    description = RichTextField(null=True, blank=True)

    university_name = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='education')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')

    def __str__(self):
        return self.major


# Kinh nghiem cua Ung vien
class ExperienceProfile(models.Model):
    job = models.CharField(max_length=100)
    position = models.CharField(max_length=255)
    time_start = models.DateField()
    time_end = models.DateField()
    company_name = models.CharField(max_length=255)
    description = RichTextField(null=True)

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='experience')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')

    def __str__(self):
        return self.job


# CV cua Ung Vien
class CVOnline(ItemBase):
    title = models.CharField(max_length=255, default="Title")
    cv = models.FileField(null=True, upload_to='CV/%Y/%m')

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='cv')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cv')

    def __str__(self):
        return self.title


# View
class BaseView(ItemBase):
    view = models.IntegerField(default=0)

    class Meta:
        abstract = True


class ViewEmployer(BaseView):
    employer = models.OneToOneField(Employer, related_name='view', on_delete=models.CASCADE)


class ViewProfile(BaseView):
    profile = models.OneToOneField(Profile, related_name='view', on_delete=models.CASCADE)



