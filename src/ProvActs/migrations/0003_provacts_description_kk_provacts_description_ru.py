# Generated by Django 5.0.2 on 2024-03-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProvActs', '0002_remove_provacts_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='provacts',
            name='description_kk',
            field=models.TextField(null=True, verbose_name='Описание правовых актов'),
        ),
        migrations.AddField(
            model_name='provacts',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание правовых актов'),
        ),
    ]
