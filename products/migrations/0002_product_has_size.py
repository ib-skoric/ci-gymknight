# Generated by Django 3.1.2 on 2020-11-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_size',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]