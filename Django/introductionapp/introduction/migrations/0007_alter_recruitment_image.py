# Generated by Django 4.0.2 on 2022-05-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0006_alter_action_created_date_alter_action_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='image',
            field=models.ImageField(null=True, upload_to='recruitment/%Y/%m'),
        ),
    ]
