# Generated by Django 3.2.25 on 2024-05-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
