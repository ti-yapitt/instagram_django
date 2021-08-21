# Generated by Django 3.2.5 on 2021-08-21 06:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0005_auto_20210816_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 21, 6, 14, 31, 316198, tzinfo=utc), null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('text', models.CharField(blank=True, max_length=300, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]
