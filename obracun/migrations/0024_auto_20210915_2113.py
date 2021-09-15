# Generated by Django 3.2.4 on 2021-09-15 19:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('obracun', '0023_alter_contract_annex_annex_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract_annex',
            name='annex_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obracun.contract'),
        ),
    ]
