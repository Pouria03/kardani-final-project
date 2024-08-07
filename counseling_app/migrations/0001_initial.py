# Generated by Django 4.2 on 2024-04-27 14:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counseling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='عنوان')),
                ('description', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'مشاوره',
                'verbose_name_plural': 'انواع مشاوره ها',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='نام کسی که فرم ثبت درخواست  در صفحه مشاوره را ثبت کرده است', max_length=60, verbose_name='نام')),
                ('user_phone', models.CharField(max_length=11, verbose_name='موبایل کاربر')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت فرم درخواست')),
                ('counseling_type', models.ForeignKey(help_text='نوع مشاوره ای که کاربر در فرمی که در صفحه مشاوره است ثبت کرده. ', null=True, on_delete=django.db.models.deletion.SET_NULL, to='counseling_app.counseling', verbose_name='نوع مشاوره درخواستی')),
            ],
            options={
                'verbose_name': ' فرم ثبت درخواست های کاربر',
                'verbose_name_plural': 'فرم های ثبت درخواست کاربران',
            },
        ),
    ]
