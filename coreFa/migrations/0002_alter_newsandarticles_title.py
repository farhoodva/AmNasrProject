# Generated by Django 4.2.2 on 2023-07-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreFa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandarticles',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
    ]
