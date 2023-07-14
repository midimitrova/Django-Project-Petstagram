from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'id', 'description')
    MIN_DESCRIPTION_LEN = 10
    MAX_DESCRIPTION_LEN = 300

    MAX_LOCATION_LEN = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        null=False,
        blank=False,
        validators=(
            validate_file_less_than_5mb,
        ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LEN),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LEN,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
