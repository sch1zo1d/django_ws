# Generated by Django 4.1.1 on 2022-09-16 16:04

from django.db import migrations, models
import exiffield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_album_preview_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo',
        ),
        migrations.AddField(
            model_name='photo',
            name='exif',
            field=exiffield.fields.ExifField(default={}, editable=False),
        ),
        migrations.AddField(
            model_name='photo',
            name='external_id',
            field=models.PositiveIntegerField(null=True, verbose_name='Photo ID'),
        ),
        migrations.AddField(
            model_name='photo',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AddField(
            model_name='photo',
            name='authors',
            field=models.ManyToManyField(to='gallery.author'),
        ),
    ]
