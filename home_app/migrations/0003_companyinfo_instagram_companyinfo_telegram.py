# Generated by Django 4.2 on 2024-04-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_companyinfo_intro_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='instagram',
            field=models.CharField(default=None, max_length=50, verbose_name='نام کاربری اکانت اینستاگرام'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='telegram',
            field=models.CharField(default='', max_length=50, verbose_name='آی دی کانال یا چت تلگرام'),
            preserve_default=False,
        ),
    ]
