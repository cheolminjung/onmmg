# Generated by Django 5.1.3 on 2024-12-02 15:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='post_photos/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='post_photos/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='post_photos/')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='post_photos/')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='post_photos/')),
                ('content', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('additional_url', models.URLField(blank=True, null=True)),
                ('address', models.CharField(max_length=255)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='omgg.post')),
            ],
        ),
    ]
