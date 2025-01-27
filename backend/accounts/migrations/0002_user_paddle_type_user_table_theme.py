# Generated by Django 4.2.8 on 2024-06-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='paddle_type',
            field=models.CharField(choices=[('B', 'Basic'), ('F', 'Fire'), ('I', 'Ice')], default='B', max_length=1, verbose_name='Paddle Type'),
        ),
        migrations.AddField(
            model_name='user',
            name='table_theme',
            field=models.CharField(choices=[('C', 'Classic'), ('S', 'Standard'), ('F', 'Football')], default='C', max_length=1, verbose_name='Table Theme'),
        ),
    ]
