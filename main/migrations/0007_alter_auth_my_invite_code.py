# Generated by Django 4.0.3 on 2022-03-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_auth_invite_code_alter_auth_my_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='my_invite_code',
            field=models.CharField(default='Gcnkg3', max_length=6),
        ),
    ]
