# Generated by Django 2.2.5 on 2021-05-31 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoCategoryModel',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('category',),
            },
        ),
        migrations.CreateModel(
            name='VideoDetailModel',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('tags', models.CharField(max_length=1000)),
                ('thumbnail', models.ImageField(upload_to='images/thumbnail/')),
                ('video', models.FileField(upload_to='video/')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.VideoCategoryModel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
