# Generated by Django 2.2.4 on 2020-07-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('head0', models.CharField(default='', max_length=500)),
                ('head1', models.CharField(default='', max_length=500)),
                ('head2', models.CharField(default='', max_length=500)),
                ('thumbnail', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='blog',
        ),
    ]
