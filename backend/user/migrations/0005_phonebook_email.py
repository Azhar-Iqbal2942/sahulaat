# Generated by Django 3.0.8 on 2020-08-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200811_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
