# Generated by Django 3.1.3 on 2020-11-11 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academy', models.TextField()),
                ('priority', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('citation', models.IntegerField(default=0, null=True)),
                ('href', models.TextField()),
                ('abstraction', models.TextField()),
                ('priority', models.IntegerField(default=0, null=True)),
                ('academy', models.ManyToManyField(to='paper_cat_model.Academy')),
                ('author', models.ManyToManyField(to='paper_cat_model.Author')),
                ('keyword', models.ManyToManyField(to='paper_cat_model.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='KeywordRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ManyToManyField(to='paper_cat_model.Keyword')),
                ('paper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paper_cat_model.paper')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper_cat_model.category')),
                ('paper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paper_cat_model.paper')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ManyToManyField(to='paper_cat_model.Author')),
                ('paper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paper_cat_model.paper')),
            ],
        ),
    ]
