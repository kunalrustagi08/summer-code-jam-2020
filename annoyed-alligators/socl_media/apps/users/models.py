from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    To contain user profile fields:
    user: holds the actual user logged in
    image: for profile picture (optional)
    bio: to update user Bio (optional)
    date_of_birth: contains user date of birth
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png",
                              upload_to="profile_pics")
    bio = models.TextField(default="I'm using socl_media", max_length=280,
                           blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Other',),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, **kwargs):
        """
        This function will resize and add a pixelating effect to the images.
        """
        super().save()

        img = Image.open(self.image.path)
        img = img.resize((48, 48), resample=Image.BILINEAR)

        output_size = (64, 64)
        img = img.resize(output_size, Image.NEAREST)
        img.thumbnail(output_size)
        img.save(self.image.path)
