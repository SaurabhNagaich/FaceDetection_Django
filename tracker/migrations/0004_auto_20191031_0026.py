# Generated by Django 2.2.6 on 2019-10-30 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20191031_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.User'),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.User'),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Task'),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.User'),
        ),
    ]
