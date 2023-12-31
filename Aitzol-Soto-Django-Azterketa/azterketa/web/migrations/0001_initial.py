# Generated by Django 3.1.4 on 2023-10-17 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etxea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.TextField()),
                ('herria', models.TextField()),
                ('pertsona_kop', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pertsona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.TextField()),
                ('emaila', models.TextField()),
                ('nan', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Alokairua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alokatze_hasiera', models.DateTimeField()),
                ('alokatze_amaiera', models.DateTimeField()),
                ('etxea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.etxea')),
                ('pertsona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.pertsona')),
            ],
        ),
    ]
