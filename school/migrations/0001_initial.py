# Generated by Django 3.2 on 2021-07-02 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('6', '6 eime'), ('5', '5 eime'), ('4', '4 eime'), ('3', '3 eime'), ('2', 'seconde'), ('1', 'premiere'), ('0', 'terminale')], max_length=2, null=True)),
                ('speciality', models.CharField(blank=True, choices=[('C', 'Mathematique'), ('D', 'Science'), ('TI', 'Informatique'), ('ALL', 'Allemand'), ('ESP', 'Espagnol'), ('N', 'None')], max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField()),
                ('matter', models.CharField(blank=True, choices=[('math', 'Mathematique'), ('phy', 'Physique'), ('chim', 'Chimie'), ('hist', 'Histoire'), ('svt', 'Science'), ('geo', 'Geographie'), ('eng', 'Anglais'), ('fr', 'Francais'), ('ecm', 'ECM'), ('stud', 'student'), ('eps', 'sport')], max_length=7, null=True)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_matter', to='school.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecon_question', to='school.lecon')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('verify', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_response', to='school.question')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('describe', models.TextField()),
                ('limit_day', models.DateField()),
                ('course_day', models.DateField()),
                ('begin_time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('status', models.BooleanField(blank=True, default=False)),
                ('matter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matter_program', to='school.matter')),
            ],
        ),
        migrations.AddField(
            model_name='lecon',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_lecon', to='school.program', unique=True),
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_classe', to='school.classe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
