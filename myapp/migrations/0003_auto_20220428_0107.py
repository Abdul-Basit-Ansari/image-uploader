# Generated by Django 3.2.8 on 2022-04-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_photo_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.AddField(
            model_name='image',
            name='sno',
            field=models.AutoField(default=3, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]