# Generated by Django 5.0.6 on 2024-07-01 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_remove_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': 'مطلب', 'verbose_name_plural': 'مطالب'},
        ),
    ]
