# Generated by Django 3.2.25 on 2025-06-25 10:48

from django.conf import settings
from django.db import migrations, transaction
from django.db.models import Q

BATCH_SIZE = 5000


def queryset_in_batches(queryset):
    """Slice a queryset into batches.

    Input queryset should be sorted be pk.
    """
    start_pk = 0

    while True:
        qs = queryset.filter(pk__gt=start_pk)[:BATCH_SIZE]
        pks = list(qs.values_list("pk", flat=True))

        if not pks:
            break

        yield pks

        start_pk = pks[-1]


def migrate_env_variable_setting_to_channels(apps, _schema_editor):
    Channel = apps.get_model("channel", "Channel")
    turn_on = int(settings.TRANSACTION_BATCH_FOR_RELEASING_FUNDS) > 0
    channels = Channel.objects.order_by("pk").filter(
        ~Q(
            checkout_ttl_before_releasing_funds=settings.CHECKOUT_TTL_BEFORE_RELEASING_FUNDS
        )
        | ~Q(release_funds_for_expired_checkouts=turn_on)
    )

    for ids in queryset_in_batches(channels):
        qs = Channel.objects.filter(pk__in=ids).order_by("pk")
        if ids:
            with transaction.atomic():
                # lock the batch of objects
                _channels = list(qs.select_for_update(of=(["self"])))
                qs.update(
                    checkout_ttl_before_releasing_funds=settings.CHECKOUT_TTL_BEFORE_RELEASING_FUNDS,
                    release_funds_for_expired_checkouts=turn_on,
                )


class Migration(migrations.Migration):
    dependencies = [
        ("channel", "0019_auto_20250625_1048"),
    ]

    operations = [
        migrations.RunPython(
            migrate_env_variable_setting_to_channels,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
