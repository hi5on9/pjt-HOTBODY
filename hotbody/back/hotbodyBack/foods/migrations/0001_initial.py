# Generated by Django 3.1.1 on 2020-10-07 15:51

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
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kcal', models.IntegerField(blank=True, null=True)),
                ('car', models.IntegerField(blank=True, null=True)),
                ('pro', models.IntegerField(blank=True, null=True)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('tsg', models.IntegerField(blank=True, null=True)),
                ('foodImg', models.ImageField(blank=True, null=True, upload_to='')),
                ('gram', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whenEat', models.IntegerField(blank=True, null=True)),
                ('eatImg', models.ImageField(blank=True, null=True, upload_to='eat/%Y/%m/%d')),
                ('date', models.CharField(max_length=100)),
                ('userNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.TextField()),
                ('diaryDate', models.CharField(max_length=100)),
                ('userNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kcal', models.IntegerField(blank=True, null=True)),
                ('car', models.IntegerField(blank=True, null=True)),
                ('pro', models.IntegerField(blank=True, null=True)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('tsg', models.IntegerField(blank=True, null=True)),
                ('gram', models.IntegerField(default=100)),
                ('eatNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.eat')),
                ('userNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
