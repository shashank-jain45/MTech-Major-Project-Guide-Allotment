# Generated by Django 5.1 on 2024-09-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocate', '0002_remove_preferenceorder_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=9191919191, max_length=10),
            preserve_default=False,
        ),
    ]