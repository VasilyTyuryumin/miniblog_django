# Generated by Django 4.2 on 2023-04-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
