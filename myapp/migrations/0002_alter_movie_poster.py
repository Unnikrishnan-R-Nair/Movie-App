# Generated by Django 5.0.1 on 2024-02-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images'),
        ),
    ]
