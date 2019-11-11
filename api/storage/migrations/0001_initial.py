# Generated by Django 2.1.11 on 2019-11-11 04:19

import common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ansible_api', '0002_auto_20190305_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='NfsStorage',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ansible_api.Project')),
                ('status', models.CharField(choices=[('CREATING', 'CREATING'), ('RUNNING', 'RUNNING'), ('ERROR', 'ERROR')], default='RUNNING', max_length=128, null=True)),
                ('vars', common.models.JsonDictTextField(default={'allow_ip': '*', 'storage_nfs_server_path': '/exports'})),
            ],
            bases=('ansible_api.project',),
        ),
    ]
