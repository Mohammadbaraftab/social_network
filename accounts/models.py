from django.db import models
from django.conf import settings


class Country(models.Model):
    name = models.CharField(max_length=50, blank=True)
    abbreviation = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.PositiveBigIntegerField(blank=True, null=True, unique=True)
    avatar = models.ImageField(blank=True, upload_to="avatar_file/")
    bio = models.TextField(blank=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name="profiles")
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['-created_time']

    def __str__(self):
        return f"{self.user.username} Profile"


class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_PC, 'pc')
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(null=True)
    last_login = models.DateTimeField(null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=DEVICE_WEB)
    device_os = models.CharField(max_length=20, blank=True)
    device_model = models.CharField(max_length=50, blank=True)
    app_version = models.CharField(max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "device"
        verbose_name = "Device"
        verbose_name_plural = "Devices"
        ordering = ['user', '-created_time']

    def __str__(self):
        return f"{self.user.username} - {self.get_device_type_display()}"