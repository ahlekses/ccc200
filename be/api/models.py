# api/models.py
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create or modify the user profile model to include additional user info
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add additional fields as needed
    
    def __str__(self):
        return self.user.username
    
    @property
    def role(self):
        # Return the first group (role) the user belongs to
        groups = self.user.groups.all()
        return groups[0].name if groups.exists() else None

# Create UserProfile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()