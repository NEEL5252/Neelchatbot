# Generated by Django 5.0.1 on 2024-03-04 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0005_alter_new_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_order',
            name='user',
        ),
    ]