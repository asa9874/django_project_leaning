# Generated by Django 4.0.3 on 2024-05-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_vo', models.IntegerField()),
                ('english_vo', models.CharField(max_length=100)),
                ('korean_vo', models.CharField(max_length=100)),
            ],
        ),
    ]