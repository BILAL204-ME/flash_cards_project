# Generated by Django 5.0.7 on 2024-07-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_cards_options_alter_cards_surah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='vrse',
        ),
        migrations.AddField(
            model_name='cards',
            name='end_verse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cards',
            name='start_verse',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
