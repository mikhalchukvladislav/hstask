# Generated by Django 4.0.3 on 2022-03-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('my_invite_code', models.CharField(default='j2jFOk', max_length=6)),
                ('invite_code', models.CharField(default='NULL', max_length=6)),
            ],
            options={
                'verbose_name': 'Авторизация',
            },
        ),
    ]
