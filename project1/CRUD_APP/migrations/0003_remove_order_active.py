# Generated by Django 5.1.1 on 2024-09-25 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_APP', '0002_rename_sr_no_order_o_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='active',
        ),
    ]
