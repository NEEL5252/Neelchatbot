# Generated by Django 5.0.1 on 2024-03-04 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0003_alter_new_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_user',
            old_name='name',
            new_name='responseId',
        ),
    ]
