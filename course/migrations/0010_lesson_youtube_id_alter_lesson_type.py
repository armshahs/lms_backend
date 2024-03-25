# Generated by Django 5.0.3 on 2024-03-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_quiz_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='type',
            field=models.CharField(choices=[('article', 'Article'), ('quiz', 'Quiz'), ('video', 'Video')], default='article', max_length=20),
        ),
    ]
