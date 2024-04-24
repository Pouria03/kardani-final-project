# Generated by Django 4.2 on 2024-04-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'مطلب', 'verbose_name_plural': 'مطالب'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=2500, verbose_name='متن مطلب'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='نحوه نمایش عنوان مطلب در نوار ادرس مرورگر', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='uploads/thumbnails/', verbose_name='تصویر اصلی مطلب'),
        ),
    ]