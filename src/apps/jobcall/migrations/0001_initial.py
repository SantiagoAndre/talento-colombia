# Generated by Django 3.0.5 on 2020-05-05 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closing_date', models.DateTimeField(verbose_name='closing date')),
                ('position', models.CharField(max_length=150, verbose_name='position')),
                ('description', models.TextField(verbose_name='description')),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'open'), (2, 'close'), (3, 'finished')], default=1, verbose_name='state')),
                ('aspirants', models.ManyToManyField(blank=True, related_name='jobcall_aspirant', to=settings.AUTH_USER_MODEL, verbose_name='aspirants')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='company')),
            ],
            options={
                'verbose_name': 'job call',
                'verbose_name_plural': 'job calls',
                'order_with_respect_to': 'closing_date',
            },
        ),
        migrations.CreateModel(
            name='AnonymousInscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='full name')),
                ('curriculum', models.FileField(upload_to='jobcall/curriculums', verbose_name='curriculum')),
                ('jobcall', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jobcall.JobCall', verbose_name='anonymous aspirants')),
            ],
        ),
    ]
