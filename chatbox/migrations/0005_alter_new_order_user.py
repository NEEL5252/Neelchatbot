# Generated by Django 5.0.1 on 2024-03-04 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0004_rename_name_new_user_responseid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_order',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chatbox.new_user'),
        ),
    ]
