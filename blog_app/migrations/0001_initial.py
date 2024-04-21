# Generated by Django 4.2 on 2024-04-20 17:56

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
                ('slug', models.SlugField(help_text='نمایش در url مرورگر', max_length=100, unique=True)),
                ('content', models.TextField(max_length=2500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='uploads/thumbnails/')),
            ],
        ),
    ]