# Generated by Django 4.1.7 on 2023-04-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='password',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
