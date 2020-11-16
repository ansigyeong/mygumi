# Generated by Django 2.2.16 on 2020-11-13 05:58

from django.db import migrations, models
import django.db.models.deletion
import territory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('order', models.IntegerField()),
                ('hint', models.TextField()),
                ('answer', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to=territory.models.course_directory_path)),
                ('territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='territory.Territory')),
            ],
        ),
    ]