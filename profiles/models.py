from django.db import models





class Profile(models.Model):
  
    email = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField( upload_to="media/", height_field=None, width_field=None, max_length=None)

