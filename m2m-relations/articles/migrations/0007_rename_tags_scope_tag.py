# Generated by Django 5.1 on 2024-08-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_scope_articles_alter_scope_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='tags',
            new_name='tag',
        ),
    ]
