# Generated by Django 5.1.1 on 2024-10-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin_app', '0002_remove_guide_date_remove_student_date_alter_date_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='guide_file_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='student_file_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
