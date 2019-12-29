# Generated by Django 3.0.1 on 2019-12-28 18:14

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('link', models.URLField(verbose_name='Link')),
                ('ttl', models.PositiveIntegerField(blank=True, default=60, verbose_name='TTL')),
                ('language', models.CharField(blank=True, max_length=20, null=True, verbose_name='Language')),
                ('last_build_date', models.DateTimeField(blank=True, null=True, verbose_name='Last Build Date')),
                ('copyright', models.CharField(blank=True, max_length=200, null=True, verbose_name='Copyright')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Image')),
                ('docs', models.URLField(blank=True, null=True, verbose_name='Docs')),
                ('web_master', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Web Master')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Pub. Date')),
                ('scan_after', models.DateTimeField(auto_now_add=True, verbose_name='Scan After DT')),
                ('terminated', models.BooleanField(default=False, verbose_name='Terminated')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feed',
                'ordering': ['-last_build_date'],
                'unique_together': {('link', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Gocha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('link', models.URLField(verbose_name='Link')),
                ('category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=50, verbose_name='Categories')),
                ('guid', models.CharField(max_length=200, verbose_name='Globally Unique Identifier')),
                ('pub_date', models.DateTimeField(verbose_name='Pub. Date')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Author')),
                ('creator', models.CharField(blank=True, max_length=100, null=True, verbose_name='Creator')),
                ('rights', models.CharField(blank=True, max_length=200, null=True, verbose_name='Rights')),
                ('enclosure', models.URLField(blank=True, max_length=500, null=True, verbose_name='Cover Image')),
                ('related_links', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=2), blank=True, null=True, size=30, verbose_name='Related URLs Representation')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('favorite', models.BooleanField(default=False, verbose_name='Favorite')),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='feeds.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feed_item',
                'ordering': ['-pub_date'],
                'unique_together': {('guid', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('text', models.TextField(max_length=300, verbose_name='Text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('feed_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feeds.FeedItem')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]