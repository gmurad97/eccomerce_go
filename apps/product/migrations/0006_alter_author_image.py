# Generated by Django 5.2 on 2025-04-07 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_gender_options_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='authors/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg', 'webp'])]),
        ),
    ]
