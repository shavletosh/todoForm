# Generated by Django 2.1.7 on 2019-04-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='clause',
            new_name='task',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('Doing', 'нужно сделать'), ('Done', 'сделано'), ('canceled', 'отменено')], default='doing', max_length=20),
        ),
    ]
