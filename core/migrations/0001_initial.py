# Generated by Django 3.0.5 on 2020-08-16 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('api_id', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('imageLink', models.CharField(max_length=200)),
                ('isbn10', models.IntegerField()),
                ('isbn13', models.IntegerField()),
                ('user', models.IntegerField()),
                ('username', models.CharField(max_length=200)),
                ('totalPages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagesRead', models.IntegerField()),
                ('dateRead', models.CharField(max_length=10)),
                ('user', models.IntegerField()),
                ('username', models.CharField(max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Book')),
            ],
        ),
    ]
