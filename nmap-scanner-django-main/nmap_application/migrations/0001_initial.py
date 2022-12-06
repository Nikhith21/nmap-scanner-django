

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.GenericIPAddressField()),
                ('mac_address', models.CharField(max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='OperativeSystemMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('accuracy', models.PositiveSmallIntegerField()),
                ('line', models.PositiveSmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_os_match', to='nmap_application.host')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(max_length=255)),
                ('portid', models.PositiveSmallIntegerField()),
                ('state', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
                ('reason_ttl', models.PositiveSmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_port', to='nmap_application.host')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='OperativeSystemClass',
            fields=[
                ('operative_system_match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='os_match_class', serialize=False, to='nmap_application.operativesystemmatch')),
                ('type', models.CharField(max_length=255)),
                ('vendor', models.CharField(max_length=255)),
                ('operative_system_family', models.CharField(max_length=255)),
                ('operative_system_generation', models.CharField(max_length=255)),
                ('accuracy', models.PositiveSmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
            ],
        ),
        migrations.CreateModel(
            name='PortService',
            fields=[
                ('port', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='port_service', serialize=False, to='nmap_application.port')),
                ('name', models.CharField(max_length=255, null=True)),
                ('product', models.CharField(max_length=255, null=True)),
                ('extra_info', models.CharField(max_length=255, null=True)),
                ('hostname', models.CharField(max_length=255, null=True)),
                ('operative_system_type', models.CharField(max_length=255, null=True)),
                ('method', models.CharField(max_length=255, null=True)),
                ('conf', models.PositiveSmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
            ],
        ),
        migrations.CreateModel(
            name='ScannerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.GenericIPAddressField()),
                ('type', models.CharField(choices=[('QS', 'Quick scan'), ('FS', 'Full scan')], default='QS', max_length=2)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
                ('hosts', models.ManyToManyField(related_name='host_history', to='nmap_application.Host')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
