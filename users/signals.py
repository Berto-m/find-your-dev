from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

def createProfile(sender, instance, created, **kwargs):
    print('############################')
    if created:
        #the insstance is sender=user
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except User.DoesNotExist:
        print('User deletion was called from CASCADE')

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)