# Generated by Django 3.2.4 on 2021-07-18 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obracun', '0017_alter_employee_municipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='canton',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='obracun.canton'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='obracun.country'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='country_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='obracun.countryentity'),
        ),
    ]
