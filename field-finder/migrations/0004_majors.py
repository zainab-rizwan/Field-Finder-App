# Generated by Django 3.2.5 on 2021-07-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_auto_20210723_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='majors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.TextField(max_length=500)),
            ],
        ),
    ]
