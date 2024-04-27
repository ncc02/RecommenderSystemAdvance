# Generated by Django 5.0.4 on 2024-04-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.IntegerField()),
                ('recent_care', models.TextField(blank=True, null=True)),
                ('recent_add', models.TextField(blank=True, null=True)),
                ('recent_buy', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_datas',
            },
        ),
    ]
