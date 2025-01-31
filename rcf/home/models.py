from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import MultiFieldPanel, FieldRowPanel, FieldPanel
from wagtail.images import get_image_model_string


class HomePage(Page):
    template = "pages/home_page.html"
    max_count = 1

    fixed_text = models.CharField(
        max_length=250,
        verbose_name="Phrase fixe",
        help_text="Début de la phrase fixe, à compléter avec les trois morceaux de la phrase pivotants",
    )
    rotating_text_A = models.CharField(
        max_length=250,
        verbose_name="Phrase pivotante 1",
        help_text="Fin de la phrase, partie pivotante n°1",
    )
    rotating_text_B = models.CharField(
        max_length=250,
        verbose_name="Phrase pivotante 2",
        help_text="Fin de la phrase, partie pivotante n°2",
    )
    rotating_text_C = models.CharField(
        max_length=250,
        verbose_name="Phrase pivotante 3",
        help_text="Fin de la phrase, partie pivotante n°3",
    )
    custom_title = models.CharField(max_length=250, verbose_name="Titre")
    subtitle = models.CharField(max_length=250, verbose_name="Sous-titre")

    cta_text_A = models.CharField(
        max_length=250, verbose_name="Titre du bouton mis en avant"
    )
    cta_link_A = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Lien du bouton",
    )

    cta_text_B = models.CharField(max_length=250, verbose_name="Titre du lien")
    cta_link_B = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Lien",
    )

    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Image",
        help_text="Cette image apparait dans le cercle à côté du titre.",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("fixed_text"),
                FieldPanel("rotating_text_A"),
                FieldPanel("rotating_text_B"),
                FieldPanel("rotating_text_C"),
            ],
            heading="Phrase pivotante",
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel([FieldPanel("custom_title"), FieldPanel("subtitle")]),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [FieldPanel("cta_text_A"), FieldPanel("cta_link_A")]
                        ),
                        FieldRowPanel(
                            [FieldPanel("cta_text_B"), FieldPanel("cta_link_B")]
                        ),
                    ]
                ),
                FieldPanel("photo"),
            ],
            heading="Titre & image",
        ),
    ]

    class Meta:
        verbose_name = "Page d'accueil"
