<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-07-01 12:44
=======
# Generated by Django 5.0.6 on 2024-06-30 14:30
>>>>>>> liarahost

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequentquestion',
            name='question',
            field=models.TextField(max_length=500, verbose_name='پرسش'),
        ),
    ]
