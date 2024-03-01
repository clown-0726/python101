# Generated by Django 3.1.4 on 2022-09-07 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('reply', models.BooleanField(default=False, verbose_name='IS REPLY')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='CREATED AT')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='UPDATED AT')),
                ('liked', models.ManyToManyField(related_name='liked_news', to=settings.AUTH_USER_MODEL, verbose_name='LIKED')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread', to='pureapp.news', verbose_name='SELF RELATED')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publisher', to=settings.AUTH_USER_MODEL, verbose_name='USER')),
            ],
            options={
                'verbose_name': 'NEWS MGT',
                'verbose_name_plural': 'NEWS MGT',
                'ordering': ('-created_at',),
            },
        ),
    ]