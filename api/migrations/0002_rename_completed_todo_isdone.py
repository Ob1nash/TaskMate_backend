# Generated by Django 5.0.6 on 2024-06-29 20:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="completed",
            new_name="isdone",
        ),
    ]
