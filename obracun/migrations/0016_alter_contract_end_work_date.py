# Generated by Django 3.2.4 on 2021-07-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obracun', '0015_rename_dutration_contract_duration_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='end_work_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]