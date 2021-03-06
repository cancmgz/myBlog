# Generated by Django 2.0.5 on 2018-05-18 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180518_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('camera', models.CharField(max_length=50)),
                ('diaphragm', models.CharField(max_length=4)),
                ('iso', models.IntegerField()),
                ('shootTime', models.CharField(max_length=8, null=True)),
                ('lens', models.CharField(max_length=100, null=True)),
                ('mode', models.CharField(max_length=10, null=True)),
                ('model', models.CharField(max_length=100, null=True)),
                ('shootDate', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('distance', models.CharField(max_length=10, null=True)),
                ('photoUrl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('isActive', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.PhotoCategory'),
        ),
    ]
