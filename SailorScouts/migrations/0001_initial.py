# Generated by Django 2.2.5 on 2023-05-04 20:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sailor_name', models.CharField(max_length=50)),
                ('english_name', models.CharField(max_length=50)),
                ('japanese_name', models.CharField(max_length=50)),
                ('sailor_power', models.CharField(max_length=50)),
            ],
            managers=[
                ('Scout', django.db.models.manager.Manager()),
            ],
        ),
    ]
