# Generated by Django 4.2 on 2023-04-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='image/%Y', verbose_name='Изображение'),
        ),
    ]