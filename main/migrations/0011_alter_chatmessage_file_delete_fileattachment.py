# Generated by Django 4.2.3 on 2023-07-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_fileattachment_remove_userip_latest_message_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.DeleteModel(
            name='FileAttachment',
        ),
    ]
