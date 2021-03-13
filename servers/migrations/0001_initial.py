# Generated by Django 3.1.3 on 2021-03-11 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('computers', '0003_computersmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=200, unique=True)),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('network', models.CharField(choices=[('GEN', 'General Network'), ('TSN', 'Technical Support Network'), ('SEC', 'Secure Network')], max_length=200)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_brand_company', to='computers.brand')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_cpu_type', to='computers.cpumodel')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_os_type', to='computers.os')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_ram_size', to='computers.ramsize')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]