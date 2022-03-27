# Generated by Django 4.0.3 on 2022-03-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_auth_my_invite_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(max_length=4)),
            ],
            options={
                'verbose_name': 'Код подтверждения',
            },
        ),
        migrations.AlterField(
            model_name='auth',
            name='my_invite_code',
            field=models.CharField(default='2Fehu1', max_length=6),
        ),
    ]
