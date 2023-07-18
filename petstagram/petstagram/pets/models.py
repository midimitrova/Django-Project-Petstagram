from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_LEN_NAME = 30
    name = models.CharField(
        max_length=MAX_LEN_NAME,
        blank=False,
        null=False,
    )

    personal_photo = models.URLField(
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)
