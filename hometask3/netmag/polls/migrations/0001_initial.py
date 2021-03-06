# Generated by Django 2.0.2 on 2018-03-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('tasktext', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_imp', models.BooleanField()),
                ('is_ready', models.BooleanField()),
            ],
        ),
    ]
