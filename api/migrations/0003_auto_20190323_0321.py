# Generated by Django 2.1.7 on 2019-03-23 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_ingredient_recipe_step'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ForeignKey(default='garlic', on_delete=django.db.models.deletion.CASCADE, to='api.Ingredient'),
        ),
        migrations.AddField(
            model_name='step',
            name='recipe',
            field=models.ForeignKey(default='dinner', on_delete=django.db.models.deletion.CASCADE, to='api.Recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='text',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_text',
            field=models.CharField(max_length=500),
        ),
        migrations.AddField(
            model_name='recipe',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.User'),
        ),
    ]