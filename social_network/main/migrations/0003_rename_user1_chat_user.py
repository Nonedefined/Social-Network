# Generated by Django 3.2.6 on 2021-08-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_chat_messagechat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='user1',
            new_name='user',
        ),
    ]
