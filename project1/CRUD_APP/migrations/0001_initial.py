# Generated by Django 5.1.1 on 2024-09-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('organization', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=60)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_updated_date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
