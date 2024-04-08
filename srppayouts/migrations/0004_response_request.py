# Generated by Django 4.2.10 on 2024-04-02 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srppayouts', '0003_alter_general_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.IntegerField(default=0)),
                ('character_name', models.CharField(blank=True, max_length=255)),
                ('corporation_id', models.IntegerField(default=0)),
                ('corporation_name', models.CharField(blank=True, max_length=255)),
                ('alliance_id', models.IntegerField(default=0)),
                ('alliance_name', models.CharField(blank=True, max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_id', models.IntegerField(default=0)),
                ('ship_name', models.CharField(blank=True, max_length=255)),
                ('character_id', models.IntegerField(default=0)),
                ('character_name', models.CharField(blank=True, max_length=255)),
                ('corporation_id', models.IntegerField(default=0)),
                ('corporation_name', models.CharField(blank=True, max_length=255)),
                ('alliance_id', models.IntegerField(default=0)),
                ('alliance_name', models.CharField(blank=True, max_length=255)),
                ('killmail_id', models.IntegerField(default=0)),
                ('killmail_time', models.CharField(blank=True, max_length=255)),
                ('killmail_solar_id', models.IntegerField(default=0)),
                ('esi_link', models.CharField(blank=True, max_length=255)),
                ('ping', models.CharField(blank=True, max_length=1023)),
                ('response', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='srppayouts.response')),
            ],
        ),
    ]