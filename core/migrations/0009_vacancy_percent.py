# Generated by Django 3.2 on 2021-05-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210507_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='percent',
            field=models.CharField(default='0', max_length=10, verbose_name='Percentage'),
        ),
    ]
