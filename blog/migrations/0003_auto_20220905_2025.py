# Generated by Django 3.2.15 on 2022-09-05 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
