# Generated by Django 3.2.10 on 2022-05-24 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("classifiers", "0004_datafileheader"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="datafileheader",
            options={"verbose_name_plural": "Data File Headers"},
        ),
    ]