# Generated by Django 2.2.1 on 2019-05-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isportbook_main', '0014_auto_20190518_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='icon',
            field=models.ImageField(null=True, upload_to='sports/'),
        ),
    ]