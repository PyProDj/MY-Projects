# Generated by Django 3.2.4 on 2021-07-29 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obracun', '0021_alter_contract_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_annex',
            name='contract_duration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='obracun.contract_duration'),
        ),
        migrations.AddField(
            model_name='contract_annex',
            name='end_work_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_annex',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
