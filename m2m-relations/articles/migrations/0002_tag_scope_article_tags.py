# Generated by Django 5.1 on 2024-08-20 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Название тега')),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='articles.article')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='articles.tag')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.tag'),
        ),
    ]
