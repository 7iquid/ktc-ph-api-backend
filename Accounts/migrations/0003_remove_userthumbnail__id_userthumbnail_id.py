# Generated by Django 4.0 on 2022-08-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_remove_userthumbnail_id_userthumbnail__id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userthumbnail',
            name='_id',
        ),
        migrations.AddField(
            model_name='userthumbnail',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
