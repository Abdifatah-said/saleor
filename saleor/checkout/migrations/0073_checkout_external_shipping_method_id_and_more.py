# Generated by Django 4.2.15 on 2025-02-10 09:57

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0072_propagate_line_undiscounted_unit_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="external_shipping_method_id",
            field=models.CharField(
                blank=True, default=None, editable=False, max_length=255, null=True
            ),
        ),
        migrations.AddField(
            model_name="checkout",
            name="shipping_method_name",
            field=models.CharField(
                blank=True, default=None, editable=False, max_length=255, null=True
            ),
        ),
        migrations.AddField(
            model_name="checkout",
            name="undiscounted_base_shipping_price_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.RunSQL(
            """
            ALTER TABLE checkout_checkout
            ALTER COLUMN undiscounted_base_shipping_price_amount
            SET DEFAULT 0;
            """,
            migrations.RunSQL.noop,
        ),
    ]
