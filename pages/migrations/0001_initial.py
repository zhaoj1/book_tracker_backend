# Generated by Django 3.0.5 on 2020-07-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagesRead', models.IntegerField()),
                ('dateRead', models.CharField(max_length=10)),
                ('book', models.IntegerField()),
                ('owner', models.IntegerField()),
            ],
        ),
    ]
