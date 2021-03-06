# Generated by Django 2.1.2 on 2019-06-23 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interno', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorios_recrutamento',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsavel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projetos',
            name='colaboradores',
            field=models.ManyToManyField(related_name='colaboradores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projetos',
            name='gestores',
            field=models.ManyToManyField(related_name='gestores', to=settings.AUTH_USER_MODEL),
        ),
    ]
