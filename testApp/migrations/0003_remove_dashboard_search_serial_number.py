# Generated by Django 4.2.4 on 2023-08-07 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_alter_dashboard_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='search_serial_number',
        ),
    ]