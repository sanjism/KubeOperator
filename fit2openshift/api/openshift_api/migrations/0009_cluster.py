# Generated by Django 2.1.2 on 2018-12-07 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_api', '0002_auto_20181207_0429'),
        ('openshift_api', '0008_auto_20181207_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ansible_api.Project')),
                ('status', models.CharField(default='idle', max_length=128)),
                ('config', models.TextField(default='')),
                ('offline', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='openshift_api.Offline')),
            ],
            bases=('ansible_api.project',),
        ),
    ]
