# Generated by Django 4.0.2 on 2022-05-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0007_alter_recruitment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='tags',
            field=models.ManyToManyField(to='introduction.Tag'),
        ),
    ]
