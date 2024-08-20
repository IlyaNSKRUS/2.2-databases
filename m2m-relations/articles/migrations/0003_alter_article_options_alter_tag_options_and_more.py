# Generated by Django 5.1 on 2024-08-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название тега'),
        ),
    ]
