# Generated by Django 4.0.3 on 2022-03-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_auth_invite_code_alter_auth_my_invite_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='my_invite_code',
            field=models.CharField(default='aqjgwx', max_length=6, unique=True),
        ),
    ]
