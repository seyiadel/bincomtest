# Generated by Django 4.1.5 on 2023-01-11 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "election_poll_app",
            "0002_rename_polling_unit_uniqueid_announced_pu_results_polling_unit_uniqueid_id",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="polling_unit",
            old_name="lga_id",
            new_name="lga_id_id",
        ),
    ]
