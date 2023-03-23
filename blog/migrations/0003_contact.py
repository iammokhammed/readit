# Generated by Django 4.1.7 on 2023-02-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=222)),
                ('message', models.TextField()),
            ],
        ),
    ]