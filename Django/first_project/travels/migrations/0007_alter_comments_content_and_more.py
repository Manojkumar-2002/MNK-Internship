# Generated by Django 5.1.5 on 2025-01-29 10:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("travels", "0006_rename_comments_comments_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="destination_deatils",
            name="area_desc",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]
