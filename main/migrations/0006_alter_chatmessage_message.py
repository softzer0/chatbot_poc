# Generated by Django 4.2.3 on 2023-07-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_chatsession_info_provided_chatsession_is_terminated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
