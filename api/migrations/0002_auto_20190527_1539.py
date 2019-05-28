# Generated by Django 2.2.1 on 2019-05-27 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewer_metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='review',
            old_name='company_id',
            new_name='company_name',
        ),
        migrations.DeleteModel(
            name='Reviewer',
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Reviewer_metadata'),
            preserve_default=False,
        ),
    ]