# Generated by Django 5.0.1 on 2024-02-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
