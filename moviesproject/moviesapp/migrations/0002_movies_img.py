# Generated by Django 4.2.1 on 2023-05-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='dfff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
