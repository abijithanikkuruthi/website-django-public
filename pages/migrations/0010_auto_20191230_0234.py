# Generated by Django 2.2.8 on 2019-12-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20191230_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]