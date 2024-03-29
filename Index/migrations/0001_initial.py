# Generated by Django 4.2.7 on 2024-03-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام کاربر')),
                ('phone', models.IntegerField(verbose_name='تلفن')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('text', models.TextField(verbose_name='متن پیام')),
            ],
            options={
                'verbose_name': 'ارتباط با ما',
                'verbose_name_plural': 'ارتباط با ما ها',
            },
        ),
    ]
