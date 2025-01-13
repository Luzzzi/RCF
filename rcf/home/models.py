from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from .blocks import StoryBlock

class BasePage(Page):
    body=StreamField(
        StoryBlock(), use_json_field=True, verbose_name="Corps de la page"
    )

class HomePage(BasePage):
    pass
