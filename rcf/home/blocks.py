from wagtail.blocks import StreamBlock, TextBlock, CharBlock, StructBlock, RichTextBlock

class QuoteBlock(StructBlock):
    quote = TextBlock(
        label="Citation",
        help_text="Les guillemets seront ajoutés automatiquement.",
    )
    author = CharBlock(label="Auteur", required=False)

    class Meta:
        icon = "openquote"
        template="blocks/quoteblock.html"

class StoryBlock(StreamBlock):
    quote=QuoteBlock()
    text=RichTextBlock()

    class Meta:
        template = "blocks/streamfield.html"