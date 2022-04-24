# Generated by Django 4.0.2 on 2022-02-26 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id_dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webdevhunterapp.developer')),
            ],
        ),
        migrations.CreateModel(
            name='Technologie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('developers', models.ManyToManyField(to='webdevhunterapp.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webdevhunterapp.client')),
                ('id_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webdevhunterapp.project')),
            ],
        ),
    ]
