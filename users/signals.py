# post_save is basically used as it gets triggered when an object is created
from django.db.models.signals import post_save
from django.contrib.auth.models import User #User is the sender > of the images
from django.dispatch import receiver
from .models import Profile

# Once the profile gets created, the receiver triggers the signal(ie post_save) and it sends all 
# the paramters including the created User instance and a profile is created for that instance.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()