# Generated by Django 2.2.7 on 2019-11-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=None),
        ),
    ]