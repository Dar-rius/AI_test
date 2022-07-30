# Generated by Django 4.0.5 on 2022-07-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message_wolof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('emotion', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=50, verbose_name='sentiments')),
            ],
        ),
        migrations.CreateModel(
            name='Sentences_wolof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
            ],
        ),
    ]
