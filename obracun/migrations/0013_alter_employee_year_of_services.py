# Generated by Django 3.2.4 on 2021-07-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obracun', '0012_alter_employee_municipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='year_of_services',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
