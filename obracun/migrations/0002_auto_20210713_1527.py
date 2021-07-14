# Generated by Django 3.2.4 on 2021-07-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obracun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='canton',
            field=models.IntegerField(blank=True, choices=[('', '---------'), (1, 'Sarajevski kanton'), (2, 'Unsko Sanski Kanton'), (3, 'Zenicko Dobojski Kanton')], null=True),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='country',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='country_entity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
