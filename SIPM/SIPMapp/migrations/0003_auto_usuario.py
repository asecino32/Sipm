# Generated by Django 3.1.4 on 2022-10-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIPMapp', '0002_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='usuario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
