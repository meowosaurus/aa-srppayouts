# Generated by Django 4.2.10 on 2024-04-08 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srppayouts', '0009_alter_request_submitted_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='general',
            options={'default_permissions': (), 'managed': False, 'permissions': (('basic_access', 'Can access this app'), ('reimburse_access', 'Can access, complete and reject reimburse requests'), ('manager_access', 'Can manage payouts'), ('admin_access', 'Can force to recalculate the table'))},
        ),
    ]
