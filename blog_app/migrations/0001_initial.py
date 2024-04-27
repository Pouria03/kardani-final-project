# Generated by Django 4.2 on 2024-04-27 14:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(help_text='نحوه نمایش عنوان مطلب در نوار ادرس مرورگر', max_length=100, unique=True)),
                ('content', ckeditor.fields.RichTextField(max_length=2500, verbose_name='متن مطلب')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='uploads/thumbnails/', verbose_name='تصویر اصلی مطلب')),
            ],
            options={
                'verbose_name': 'مطلب',
                'verbose_name_plural': 'مطالب',
            },
        ),
    ]
