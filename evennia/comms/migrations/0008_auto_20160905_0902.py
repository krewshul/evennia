# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-05 09:02


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("comms", "0007_msg_db_tags")]

    operations = [
        migrations.AlterModelOptions(name="msg", options={"verbose_name": "Msg"}),
        migrations.RenameField(
            model_name="msg", old_name="db_date_sent", new_name="db_date_created"
        ),
    ]
