from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.TextBlock()
    background_image = ImageChooserBlock(required=False)

    class Meta:
        icon = "image"
        template = "core/blocks/hero_section_block.html"
        label = "Hero Section"
