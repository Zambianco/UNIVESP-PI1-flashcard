# Generated by Django 3.2.7 on 2021-09-12 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Disciplinas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.CharField(max_length=200)),
                ('define', models.TextField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disciplinas.disciplina')),
            ],
        ),
    ]
