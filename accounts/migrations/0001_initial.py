# Generated by Django 4.2 on 2024-11-29 21:35

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
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('abbreviation', models.CharField(blank=True, max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveBigIntegerField(blank=True, null=True, unique=True)),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/')),
                ('bio', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='accounts.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'profile',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uuid', models.UUIDField(null=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('device_type', models.PositiveSmallIntegerField(choices=[(1, 'web'), (2, 'ios'), (3, 'android'), (4, 'pc')], default=1)),
                ('device_os', models.CharField(blank=True, max_length=20)),
                ('device_model', models.CharField(blank=True, max_length=50)),
                ('app_version', models.CharField(blank=True, max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'db_table': 'device',
                'ordering': ['user', '-created_time'],
            },
        ),
    ]
