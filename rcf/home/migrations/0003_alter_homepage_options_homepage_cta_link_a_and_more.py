# Generated by Django 5.1.5 on 2025-01-31 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_create_homepage"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Page d'accueil"},
        ),
        migrations.AddField(
            model_name="homepage",
            name="cta_link_A",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Lien du bouton",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="cta_link_B",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Lien",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="cta_text_A",
            field=models.CharField(
                default=(), max_length=250, verbose_name="Titre du bouton mis en avant"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="cta_text_B",
            field=models.CharField(
                default=(), max_length=250, verbose_name="Titre du lien"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="fixed_text",
            field=models.CharField(
                default=(),
                help_text="Début de la phrase fixe, à compléter avec les trois morceaux de la phrase pivotants",
                max_length=250,
                verbose_name="Phrase fixe",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="Cette image apparait dans le cercle à côté du titre.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="rotating_text_A",
            field=models.CharField(
                default=(),
                help_text="Fin de la phrase, partie pivotante n°1",
                max_length=250,
                verbose_name="Phrase pivotante 1",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="rotating_text_B",
            field=models.CharField(
                default=(),
                help_text="Fin de la phrase, partie pivotante n°2",
                max_length=250,
                verbose_name="Phrase pivotante 2",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="rotating_text_C",
            field=models.CharField(
                default=(),
                help_text="Fin de la phrase, partie pivotante n°3",
                max_length=250,
                verbose_name="Phrase pivotante 3",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="subtitle",
            field=models.CharField(default=(), max_length=250, verbose_name="Subtitle"),
            preserve_default=False,
        ),
    ]
