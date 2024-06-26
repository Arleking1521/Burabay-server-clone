# Generated by Django 5.0.2 on 2024-03-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_postattachment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_kk',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Title'),
        ),
    ]
