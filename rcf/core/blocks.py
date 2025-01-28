from wagtail.blocks import (
    RichTextBlock,
    StreamBlock,
    PageChooserBlock,
    StructBlock,
    URLBlock,
    CharBlock,
    EmailBlock,
    ListBlock,
    TextBlock,
)
from wagtail.embeds import embeds
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock, EmbedValue
from core.constants import MEDIA_ITEMS_GROUP, BASE_ITEMS_GROUP, EDITORIAL_ITEMS_GROUP


class EmbedValueEnhanced(EmbedValue):
    """
    Override default EmbedValue class in order to add some properties that are
    part of the Embed object (thumbnail_url, title...).
    """

    def __init__(self, url, max_width=None, max_height=None):
        embed = embeds.get_embed(url)
        self.thumbnail_url = embed.thumbnail_url
        self.provider_name = embed.provider_name
        self.title = embed.title
        self.url = url
        self.max_width = max_width
        self.max_height = max_height


class EmbedBlockEnhanced(EmbedBlock):
    def get_default(self):
        # Allow specifying the default for an EmbedBlock as either an EmbedValue or a string (or None).
        if not self.meta.default:
            return None
        elif isinstance(self.meta.default, EmbedValue):
            return self.meta.default
        else:
            # assume default has been passed as a string
            return EmbedValueEnhanced(
                self.meta.default,
                getattr(self.meta, "max_width", None),
                getattr(self.meta, "max_height", None),
            )

    def to_python(self, value):
        # The JSON representation of an EmbedBlock's value is a URL string;
        # this should be converted to an EmbedValue (or None).
        if not value:
            return None
        else:
            return EmbedValueEnhanced(
                value,
                getattr(self.meta, "max_width", None),
                getattr(self.meta, "max_height", None),
            )

    def value_from_form(self, value):
        # convert the value returned from the form (a URL string) to an EmbedValue (or None)
        if not value:
            return None
        else:
            return EmbedValueEnhanced(
                value,
                getattr(self.meta, "max_width", None),
                getattr(self.meta, "max_height", None),
            )


class VideoItemBlock(StructBlock):
    embed = EmbedBlockEnhanced(label="Lien de la vidéo")
    caption = CharBlock(label="Légende", required=False)

    class Meta:
        icon = "media"


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "components/streamfield/blocks/image_block.html"


class LinksBlock(StreamBlock):
    internal = PageChooserBlock(label="Lien interne")
    external = URLBlock(label="Lien externe")
    email = EmailBlock(label="Email")

    class Meta:
        max_num = 1


class ButtonBlock(StructBlock):
    cta_text = CharBlock(label="Texte du bouton")
    cta_link = LinksBlock(label="Lien du bouton")


class QuoteBlock(StructBlock):
    quote = TextBlock(
        label="Citation",
        help_text="Les guillemets seront ajoutés automatiquement.",
    )
    author = CharBlock(label="Auteur", required=False)
    image = ImageChooserBlock(required=False, label="Image de profil")

    class Meta:
        icon = "openquote"


class RotatingTextBlock(StructBlock):
    text = CharBlock(label="Texte fixe")
    items = ListBlock(CharBlock(label="Texte flottant"), min_num=3, max_num=3)

    class Meta:
        template = "./components/rotating_text.html"


class StoryBlock(StreamBlock):
    rich_text = RichTextBlock(
        label="Texte riche",
        features=["h2", "h3", "h4", "bold", "hr", "italic", "link", "ol", "ul"],
        group=BASE_ITEMS_GROUP,
    )
    quote = QuoteBlock(label="Citation", group=EDITORIAL_ITEMS_GROUP)
    carousel = ListBlock(
        ImageBlock,
        label="Carousel",
        group=MEDIA_ITEMS_GROUP,
        icon="image",
    )
    image = ImageBlock(label="Image", group=MEDIA_ITEMS_GROUP)
    video = VideoItemBlock(label="Video", group=MEDIA_ITEMS_GROUP)
    rotating = RotatingTextBlock(
        label="Roulette de textes", group=EDITORIAL_ITEMS_GROUP
    )
