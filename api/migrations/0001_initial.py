# Generated by Django 3.0.5 on 2020-04-05 22:21

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='noname', max_length=255)),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('last_degree', models.CharField(blank=True, choices=[('DI', 'Diploma'), ('BA', 'Bachelor'), ('MA', 'Master'), ('DO', 'Doctorate'), ('PD', 'Post Doctorate'), ('FR', 'Free')], default='FR', max_length=255, null=True)),
                ('major', models.CharField(blank=True, max_length=255, null=True)),
                ('activity', models.CharField(blank=True, choices=[('1', 'Online'), ('0', 'Offline')], default='0', max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('institute', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('expertise', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mail', models.CharField(blank=True, max_length=255, null=True)),
                ('mail_verify', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'Disabled')], default='0', max_length=255, null=True)),
                ('tracking_code', models.CharField(blank=True, max_length=255, null=True)),
                ('agent', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('registration_date', models.CharField(blank=True, max_length=255, null=True)),
                ('pic', models.CharField(blank=True, max_length=255, null=True)),
                ('point', models.CharField(blank=True, choices=[('SA', 'Send Article'), ('JV', 'Just Visit')], default='SA', max_length=255, null=True)),
                ('pay_sts', models.CharField(blank=True, choices=[('P', 'Paid'), ('U', 'Unpaid'), ('W', 'Waiting')], default='W', max_length=255, null=True)),
                ('scan_id', models.CharField(blank=True, max_length=255, null=True)),
                ('scan_bc', models.CharField(blank=True, max_length=255, null=True)),
                ('document_validation_sts', models.CharField(blank=True, choices=[('Y', 'Validate'), ('N', 'Unvalidate')], default='N', max_length=1, null=True)),
                ('acl', models.CharField(blank=True, choices=[('US', 'User'), ('WS', 'Workshop'), ('SCI', 'Scientific Committee '), ('EXE', 'Executive Committee'), ('DB', 'Dabir'), ('DV', 'Davar'), ('WR', 'Writer'), ('NZ', 'Nazer'), ('AD', 'Admin'), ('SU', 'SuperAdministrator')], default='US', max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]