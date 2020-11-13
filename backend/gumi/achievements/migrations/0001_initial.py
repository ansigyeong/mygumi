# Generated by Django 2.2.16 on 2020-11-13 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jinpyeong', models.BooleanField(default=False)),
                ('geumosan', models.BooleanField(default=False)),
                ('bicycle', models.BooleanField(default=False)),
                ('seowon', models.BooleanField(default=False)),
                ('explorer', models.BooleanField(default=False)),
                ('korean', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
