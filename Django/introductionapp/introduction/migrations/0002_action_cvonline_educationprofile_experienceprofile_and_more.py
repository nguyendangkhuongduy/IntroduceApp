# Generated by Django 4.0.2 on 2022-05-18 08:39

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'like'), (1, 'dislike')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CVOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(default='Title', max_length=255)),
                ('cv', models.FileField(null=True, upload_to='CV/%Y/%m')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EducationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('time_start', models.DateField()),
                ('time_completed', models.DateField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=255)),
                ('time_start', models.DateField()),
                ('time_end', models.DateField()),
                ('company_name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ViewEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('view', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('view', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='active',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='employer',
            name='address_details',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='number',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='Role',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employer', to='introduction.address'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction.employer'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='tags',
            field=models.ManyToManyField(to='introduction.Tag'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='viewprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='view', to='introduction.profile'),
        ),
        migrations.AddField(
            model_name='viewemployer',
            name='employer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='view', to='introduction.employer'),
        ),
        migrations.AddField(
            model_name='experienceprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='introduction.profile'),
        ),
        migrations.AddField(
            model_name='educationprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='introduction.profile'),
        ),
        migrations.AddField(
            model_name='educationprofile',
            name='university_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='introduction.university'),
        ),
        migrations.AddField(
            model_name='cvonline',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cv', to='introduction.profile'),
        ),
        migrations.AddField(
            model_name='cvonline',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cv', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction.employer'),
        ),
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
