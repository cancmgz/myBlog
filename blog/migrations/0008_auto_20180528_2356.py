# Generated by Django 2.0.5 on 2018-05-28 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180528_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='commentReply',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.PostComment'),
        ),
    ]