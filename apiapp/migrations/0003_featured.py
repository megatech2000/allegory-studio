# Generated by Django 4.2.4 on 2024-06-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_work_home_image_work_image_1_work_image_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=400, unique=True)),
                ('title', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(default='Image/None/Noimg.jpg', upload_to='Image/')),
                ('num_1', models.TextField()),
                ('num_2', models.TextField()),
                ('num_3', models.TextField()),
            ],
        ),
    ]