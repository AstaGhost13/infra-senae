# Generated by Django 5.1.6 on 2025-03-09 18:48

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_structure', '0003_position_custodiam'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Custodian',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=60, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('reference', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reference')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(blank=True, default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custodians', to='organizational_structure.position', verbose_name='Cargo')),
                ('updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Custodio',
                'verbose_name_plural': 'Custodios',
                'db_table': 'tb_security_custodian',
            },
        ),
        migrations.DeleteModel(
            name='Custodiam',
        ),
    ]
