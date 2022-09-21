# Generated by Django 4.1.1 on 2022-09-19 15:27

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('type', models.CharField(choices=[('BACK-END', 'Back-End'), ('FRONT-END', 'Front-End'), ('IOS', 'iOS'), ('ANDROID', 'Android')], max_length=30, verbose_name='type of project')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=2048)),
                ('tag', models.CharField(choices=[('BUG', 'Bug'), ('ENHANCEMENT', 'Enhancement'), ('TASK', 'Task')], max_length=128, verbose_name='tag')),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=128, verbose_name='priority')),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('ASSIGNED', 'Assigned'), ('DONE', 'Done')], max_length=128, verbose_name='status')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_issues', to='tickets.project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_comments', to='tickets.issue')),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('CONTRIBUTOR', 'Contributor'), ('AUTHOR', 'Author')], max_length=30, verbose_name='Rôle')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'project')},
            },
        ),
    ]