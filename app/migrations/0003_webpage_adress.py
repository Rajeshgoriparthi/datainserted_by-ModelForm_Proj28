# Generated by Django 4.1.7 on 2023-04-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='adress',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
