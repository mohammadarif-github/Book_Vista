# Generated by Django 5.0.1 on 2024-03-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='book_photos/'),
        ),
    ]
