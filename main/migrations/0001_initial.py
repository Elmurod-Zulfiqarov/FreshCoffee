# Generated by Django 4.0.3 on 2022-04-11 08:08

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.SmallIntegerField(unique=True)),
                ('review', models.TextField(default=None, max_length=2048)),
                ('check_display', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=64)),
                ('discount', models.CharField(blank=True, max_length=64, null=True)),
                ('image', models.ImageField(default='menu_pics/default_menu.jpg', upload_to=main.models.Menu.dp_rename_and_path)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.CharField(max_length=64)),
                ('discount', models.CharField(blank=True, max_length=64, null=True)),
                ('image', models.ImageField(default='products_pics/default_product.jpg', upload_to=main.models.Products.dp_rename_and_path)),
            ],
        ),
    ]
