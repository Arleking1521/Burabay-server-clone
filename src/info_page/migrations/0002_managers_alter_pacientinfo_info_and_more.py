# Generated by Django 5.0.2 on 2024-03-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('post', models.TextField(verbose_name='Post')),
                ('phone', models.CharField(verbose_name='Phone number')),
                ('email', models.CharField(verbose_name='E-mail')),
                ('show', models.BooleanField(verbose_name='Show this person in second table?')),
            ],
        ),
        migrations.AlterField(
            model_name='pacientinfo',
            name='info',
            field=models.TextField(verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='pacientinfo',
            name='title',
            field=models.CharField(verbose_name='Title'),
        ),
    ]
