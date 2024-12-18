# Generated by Django 5.1.2 on 2024-10-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(null=True, upload_to='movie_images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=200),
        ),
    ]
