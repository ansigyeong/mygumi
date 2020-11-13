# Generated by Django 2.2.16 on 2020-11-13 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tour.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.IntegerField()),
                ('course_name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to=tour.models.course_directory_path)),
                ('content', models.TextField()),
                ('dong', models.CharField(max_length=50)),
                ('time', models.TextField(default='')),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Place')),
            ],
        ),
        migrations.CreateModel(
            name='CustomMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
