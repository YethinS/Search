# Generated by Django 3.1.2 on 2020-12-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
