# Generated by Django 3.0.2 on 2020-03-23 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarNuber', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Surname', models.CharField(max_length=255)),
                ('idTelegram', models.CharField(max_length=255)),
                ('MobileNumber', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='carnumbers',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='carnumbers',
            name='Surname',
        ),
        migrations.CreateModel(
            name='Parks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateInput', models.DateTimeField()),
                ('DateOutput', models.DateTimeField()),
                ('Pay', models.BooleanField(default=False)),
                ('idNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Numbers')),
            ],
        ),
        migrations.AddField(
            model_name='numbers',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Users'),
        ),
    ]