# Generated by Django 5.2.1 on 2025-07-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attribute", "0050_alter_attribute_input_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="attributevalue",
            name="numeric",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
