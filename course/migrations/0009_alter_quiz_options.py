# Generated by Django 5.0.3 on 2024-03-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_category_options_quiz'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
    ]
