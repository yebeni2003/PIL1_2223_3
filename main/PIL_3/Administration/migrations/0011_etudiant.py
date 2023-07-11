# Generated by Django 4.2.3 on 2023-07-10 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0010_emploi_published_alter_matiere_bgcolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('matricule_Etu', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_Etu', models.CharField(max_length=50)),
                ('prenom_Etu', models.CharField(max_length=100)),
                ('sexe_Etu', models.CharField(max_length=1)),
                ('date_nais_Etu', models.DateField(null=True)),
                ('age_Etu', models.IntegerField()),
                ('contact', models.IntegerField(unique=True)),
                ('email_Etu', models.EmailField(max_length=254, unique=True)),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.filiere')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]