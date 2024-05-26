# Generated by Django 4.2.13 on 2024-05-26 11:34

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('creation_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='1', max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('creation_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
