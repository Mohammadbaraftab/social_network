from django.db import models
from django.conf import settings


class Friendship(models.Model):
    request_from = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                                related_name="request_from_user")
    request_to = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                                     related_name="request_to_user")
    is_accepted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "friendship"
        verbose_name = "Friendship"
        verbose_name_plural = "Friendship"
        unique_together = ('request_from', 'request_to')

    
    def __str__(self):
        return f"{self.request_from.username} -> {self.request_to.username} (Accepted: {self.is_accepted})"