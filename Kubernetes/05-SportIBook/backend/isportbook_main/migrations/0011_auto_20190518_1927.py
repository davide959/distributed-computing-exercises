# Generated by Django 2.2.1 on 2019-05-18 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isportbook_main', '0010_auto_20190518_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isportbook_main.Profile'),
        ),
    ]
