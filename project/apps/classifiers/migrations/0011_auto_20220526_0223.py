# Generated by Django 3.2.10 on 2022-05-26 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("classifiers", "0010_auto_20220526_0220"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="datafile",
            table="classifiers_data_file",
        ),
        migrations.AlterModelTable(
            name="datafileheader",
            table="classifiers_data_file_header",
        ),
        migrations.AlterModelTable(
            name="predictioninputdata",
            table="classifiers_prediction_input_data",
        ),
    ]