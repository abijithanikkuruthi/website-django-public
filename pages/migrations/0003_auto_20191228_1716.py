# Generated by Django 2.2.8 on 2019-12-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_blog_img_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img_thumbnail',
            field=models.CharField(default='images/blog-1.jpg', max_length=200),
        ),
    ]