# Generated by Django 4.2.7 on 2024-03-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0007_newsuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsuser',
            name='Email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
    ]
