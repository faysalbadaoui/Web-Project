# Generated by Django 4.1.5 on 2023-05-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_user', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('email_user', models.EmailField(default='defaultUserMail', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('profile_photo', models.BinaryField(blank=True, null=True)),
                ('groups_number', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='departments', to='web.department')),
                ('projects', models.ManyToManyField(blank=True, related_name='projects', to='web.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]