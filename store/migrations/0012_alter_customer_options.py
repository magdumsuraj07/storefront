# Generated by Django 4.0.2 on 2022-02-23 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
