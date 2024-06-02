# Generated by Django 4.2.13 on 2024-06-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='days_left',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.CharField(choices=[('M', 'Средне'), ('H', 'Важно'), ('L', 'Не важно')], default='L', max_length=1),
        ),
    ]
