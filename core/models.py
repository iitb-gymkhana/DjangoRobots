from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ Defines a one to one mapping to User field to store additonal info such as the starting user is associated with, or any other domains user might have. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proxy = models.CharField(verbose_name='proxy', max_length=20, blank=False)
    # validate_comma_separated_integer_list for alt_domain
    alt_domain = models.CharField(
        max_length=100, blank=True, verbose_name="Alternate domains", help_text="If more than one domain, seperate by a comma(,)")

    # TODO: Do not allow user to change his own profile
    def save(self, *args, **kwargs):
        if not self.proxy.startswith('/'):
            self.proxy = '/' + self.proxy
        super(UserProfile, self).save(*args, **kwargs)
