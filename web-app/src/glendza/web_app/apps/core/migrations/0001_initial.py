# Generated by Django 5.1.4 on 2025-01-11 23:44

import django.db.models.deletion
import modelcluster.fields
import uuid
import wagtail.fields
import wagtail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "content",
                    wagtail.fields.StreamField(
                        [("hero_section", 3)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {}),
                            1: ("wagtail.blocks.TextBlock", (), {}),
                            2: ("wagtail.images.blocks.ImageChooserBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 0), ("description", 1), ("background_image", 2)]],
                                {},
                            ),
                        },
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "home page",
                "verbose_name_plural": "home pages",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField(allow_unicode=True, max_length=25, verbose_name="slug")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MainNavigationMenuSetting",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "site",
                    models.OneToOneField(
                        editable=False, on_delete=django.db.models.deletion.CASCADE, to="wagtailcore.site"
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="core.menu",
                    ),
                ),
            ],
            options={
                "verbose_name": "Main Navigation Menu",
            },
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                ("link_title", models.CharField(blank=True, max_length=50, null=True)),
                ("link_url", models.CharField(blank=True, max_length=500, null=True)),
                ("open_in_new_tab", models.BooleanField(blank=True, default=False)),
                (
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_items",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="menu_items", to="core.menu"
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FooterContent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("translation_key", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("live", models.BooleanField(default=True, editable=False, verbose_name="live")),
                (
                    "has_unpublished_changes",
                    models.BooleanField(default=False, editable=False, verbose_name="has unpublished changes"),
                ),
                (
                    "first_published_at",
                    models.DateTimeField(blank=True, db_index=True, null=True, verbose_name="first published at"),
                ),
                (
                    "last_published_at",
                    models.DateTimeField(editable=False, null=True, verbose_name="last published at"),
                ),
                ("go_live_at", models.DateTimeField(blank=True, null=True, verbose_name="go live date/time")),
                ("expire_at", models.DateTimeField(blank=True, null=True, verbose_name="expiry date/time")),
                ("expired", models.BooleanField(default=False, editable=False, verbose_name="expired")),
                ("copyright_text", wagtail.fields.RichTextField()),
                ("github_url", models.URLField(blank=True, null=True)),
                (
                    "latest_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="latest revision",
                    ),
                ),
                (
                    "live_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="live revision",
                    ),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                        verbose_name="locale",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Footer Content",
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
        migrations.CreateModel(
            name="HeaderContent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("translation_key", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("live", models.BooleanField(default=True, editable=False, verbose_name="live")),
                (
                    "has_unpublished_changes",
                    models.BooleanField(default=False, editable=False, verbose_name="has unpublished changes"),
                ),
                (
                    "first_published_at",
                    models.DateTimeField(blank=True, db_index=True, null=True, verbose_name="first published at"),
                ),
                (
                    "last_published_at",
                    models.DateTimeField(editable=False, null=True, verbose_name="last published at"),
                ),
                ("go_live_at", models.DateTimeField(blank=True, null=True, verbose_name="go live date/time")),
                ("expire_at", models.DateTimeField(blank=True, null=True, verbose_name="expiry date/time")),
                ("expired", models.BooleanField(default=False, editable=False, verbose_name="expired")),
                (
                    "latest_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="latest revision",
                    ),
                ),
                (
                    "live_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="live revision",
                    ),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                        verbose_name="locale",
                    ),
                ),
                (
                    "logo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Header Content",
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
    ]