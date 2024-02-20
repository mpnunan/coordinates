# Generated by Django 4.1.3 on 2024-02-20 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReceptionTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinatesapi.planner')),
            ],
        ),
        migrations.CreateModel(
            name='TableGuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_guests', to='coordinatesapi.guest')),
                ('reception_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_tables', to='coordinatesapi.receptiontable')),
            ],
        ),
        migrations.AddField(
            model_name='receptiontable',
            name='wedding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinatesapi.wedding'),
        ),
        migrations.AddField(
            model_name='guest',
            name='wedding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='coordinatesapi.wedding'),
        ),
    ]
