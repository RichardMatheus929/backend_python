# Generated by Django 5.0.7 on 2024-08-07 03:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0005_rename_data_nascimento_pessoa_date_born_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
