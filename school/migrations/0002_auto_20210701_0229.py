# Generated by Django 3.2 on 2021-07-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='level',
            field=models.CharField(blank=True, choices=[('6', '6 eime'), ('5', '5 eime'), ('4', '4 eime'), ('3', '3 eime'), ('2', 'seconde'), ('1', 'premiere'), ('0', 'terminale')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='classe',
            name='speciality',
            field=models.CharField(blank=True, choices=[('C', 'Mathematique'), ('D', 'Physique'), ('TI', 'Chimie'), ('ALL', 'Histoire'), ('ESP', 'Science'), ('CH', 'ECM')], max_length=7, null=True),
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Speciality',
        ),
    ]