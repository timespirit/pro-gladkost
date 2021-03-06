# Generated by Django 2.0.7 on 2018-07-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('description', models.TextField(max_length=10240, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Блог',
                'verbose_name': 'Блог',
            },
        ),
    ]
