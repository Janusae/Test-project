# Generated by Django 4.2.7 on 2024-03-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=100, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': 'کاربر دنبال کننده',
                'verbose_name_plural': 'کاربر های دنبال کننده',
            },
        ),
    ]
