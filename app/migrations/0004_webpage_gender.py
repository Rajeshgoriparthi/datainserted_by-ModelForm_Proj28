# Generated by Django 4.1.7 on 2023-04-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_webpage_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='gender',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
