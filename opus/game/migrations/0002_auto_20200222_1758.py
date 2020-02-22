# Generated by Django 3.0.2 on 2020-02-22 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('description', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='story_answer',
            name='option_1',
        ),
        migrations.RemoveField(
            model_name='story_answer',
            name='option_2',
        ),
        migrations.RemoveField(
            model_name='story_answer',
            name='option_3',
        ),
        migrations.AddField(
            model_name='story_question',
            name='on_bad',
            field=models.IntegerField(default=1003),
        ),
        migrations.AddField(
            model_name='story_question',
            name='on_good',
            field=models.IntegerField(default=1001),
        ),
        migrations.AddField(
            model_name='story_question',
            name='on_medium',
            field=models.IntegerField(default=1002),
        ),
        migrations.AlterField(
            model_name='story_answer',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Story_Question'),
        ),
        migrations.AlterField(
            model_name='story_question',
            name='choice_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='story_question',
            name='choice_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='story_question',
            name='choice_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='story_question',
            name='question_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='Aptitude_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(default=1)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Story_Question')),
            ],
        ),
        migrations.AddField(
            model_name='story_answer',
            name='choice_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='option_1', to='game.Levels'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story_answer',
            name='choice_2',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='option_2', to='game.Levels'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story_answer',
            name='choice_3',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='option_3', to='game.Levels'),
            preserve_default=False,
        ),
    ]
