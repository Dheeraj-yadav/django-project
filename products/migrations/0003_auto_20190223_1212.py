# Generated by Django 2.1 on 2019-02-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]