# Generated by Django 4.2.3 on 2023-07-10 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0011_etudiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='bgColor',
            field=models.CharField(blank=True, default='#FF8C00', max_length=100, null=True),
        ),
    ]
