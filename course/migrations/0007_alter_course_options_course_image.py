# Generated by Django 5.0.3 on 2024-03-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
