# Generated by Django 4.1 on 2023-07-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countInStock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
