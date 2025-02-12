from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from core.blocks import StoryBlock, MenuBlock
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from django.conf import settings
from django.utils.functional import cached_property


class StandardPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "pages/standard_page.html"

    body = StreamField(StoryBlock, verbose_name="Corps de page")

    class Meta:
        verbose_name = "Page standard"


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", on_delete=models.CASCADE, related_name="form_fields")


class FormPage(AbstractEmailForm):
    parent_page_types = ["home.HomePage"]
    max_count = 1
    template = "pages/form_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]


@register_setting
class MenusSettings(BaseGenericSetting):
    main_menu = StreamField(
        [("menu_item", MenuBlock(label="Item"))],
        max_num=6,
        verbose_name="Menu principal",
        collapsed=True,
        use_json_field=True,
    )
    button_title = models.CharField(
        verbose_name="Texte du bouton principal",
        max_length=25,
    )
    button = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Lien du bouton principal",
    )

    @cached_property
    def home(self):
        return settings.BASE_URL

    class Meta:
        verbose_name = "Menu principal"


@register_setting
class FooterSettings(BaseGenericSetting):
    text = RichTextField(verbose_name="Texte du footer")
    linkedin = models.URLField(verbose_name="Linkedin")
    email = models.EmailField(verbose_name="Adresse mail")

    class Meta:
        verbose_name = "Pied de page"
