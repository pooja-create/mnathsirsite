# Generated by Django 2.2.4 on 2019-09-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('projectimage', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=500)),
            ],
        ),
    ]