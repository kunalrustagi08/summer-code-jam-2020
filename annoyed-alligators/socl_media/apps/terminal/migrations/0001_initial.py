# Generated by Django 3.0.8 on 2020-08-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('search_topic', models.CharField(max_length=50)),
                ('search_time', models.DateTimeField(auto_now=True)),
                ('last_fetched_count', models.IntegerField()),
                ('news_articles', models.TextField()),
            ],
        ),
    ]
