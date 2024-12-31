# Generated by Django 5.1.4 on 2024-12-31 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('numero_siret', models.BigIntegerField(null=True)),
                ('code_postal', models.CharField(max_length=5)),
                ('adresse', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('chevaux', models.IntegerField()),
                ('immatriculation', models.CharField(max_length=10, unique=True)),
                ('date_mise_en_service', models.DateField()),
                ('concession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='api.concession')),
            ],
        ),
    ]
