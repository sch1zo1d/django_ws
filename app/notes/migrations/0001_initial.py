# Generated by Django 4.1.1 on 2022-09-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя пользователя')),
                ('external_id', models.PositiveIntegerField(verbose_name='Telegram user ID')),
            ],
        ),
    ]