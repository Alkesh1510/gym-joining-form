# Generated by Django 4.1 on 2022-08-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_emil_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=12),
        ),
    ]