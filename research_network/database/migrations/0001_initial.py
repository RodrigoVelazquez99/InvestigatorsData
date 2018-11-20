# Generated by Django 2.1.3 on 2018-11-15 18:27

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
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_campus', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Campus',
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id_college', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'College',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id_event', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id_group', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Institutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_institute', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Campus')),
            ],
            options={
                'db_table': 'Institutes',
            },
        ),
        migrations.CreateModel(
            name='Join_Group',
            fields=[
                ('id_join_group', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Join_Group',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_event', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Events')),
            ],
            options={
                'db_table': 'Log',
            },
        ),
        migrations.CreateModel(
            name='Modify_Place',
            fields=[
                ('id_modify_place', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('id_campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Campus')),
                ('id_institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Institutes')),
            ],
            options={
                'db_table': 'Modify_Place',
            },
        ),
        migrations.CreateModel(
            name='Modify_User',
            fields=[
                ('id_modify_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=128)),
                ('academic_level', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('personal_telephone', models.IntegerField()),
                ('id_institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Institutes')),
            ],
            options={
                'db_table': 'Modify_User',
            },
        ),
        migrations.CreateModel(
            name='New_User',
            fields=[
                ('id_new_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=128)),
                ('academic_level', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('personal_telephone', models.IntegerField()),
                ('id_institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Institutes')),
            ],
            options={
                'db_table': 'New_User',
            },
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id_paper', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=200)),
                ('publication_date', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=200)),
                ('binary', models.BinaryField()),
            ],
            options={
                'db_table': 'Papers',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id_people', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=128)),
                ('academic_level', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('personal_telephone', models.CharField(max_length=200)),
                ('groups', models.ManyToManyField(to='database.Groups')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Institutes')),
            ],
            options={
                'db_table': 'People',
            },
        ),
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.BooleanField()),
                ('id_institute', models.BooleanField()),
                ('id_subinstitute', models.BooleanField()),
                ('academic_level', models.BooleanField()),
                ('degree', models.BooleanField()),
                ('name', models.BooleanField()),
                ('last_name', models.BooleanField()),
                ('personal_telephone', models.BooleanField()),
                ('id_people', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.People')),
            ],
            options={
                'db_table': 'Public',
            },
        ),
        migrations.CreateModel(
            name='Register_Place',
            fields=[
                ('id_register_place', models.AutoField(primary_key=True, serialize=False)),
                ('type_place', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Register_Place',
            },
        ),
        migrations.CreateModel(
            name='Remove_Document',
            fields=[
                ('id_remove_document', models.AutoField(primary_key=True, serialize=False)),
                ('id_paper', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Papers')),
            ],
            options={
                'db_table': 'Remove_Document',
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id_request', models.AutoField(primary_key=True, serialize=False)),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Events')),
                ('id_people_receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.People')),
            ],
            options={
                'db_table': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id_state', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'States',
            },
        ),
        migrations.CreateModel(
            name='Subinstitutes',
            fields=[
                ('id_subinstitute', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('id_reference_sub', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Subinstitutes')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Institutes')),
            ],
            options={
                'db_table': 'Subinstitutes',
            },
        ),
        migrations.CreateModel(
            name='Upload_Document',
            fields=[
                ('id_upload_document', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=200)),
                ('publication_date', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=200)),
                ('binary', models.BinaryField()),
            ],
            options={
                'db_table': 'Upload_Document',
            },
        ),
        migrations.CreateModel(
            name='User_profiles',
            fields=[
                ('id_user_profile', models.AutoField(primary_key=True, serialize=False)),
                ('profile', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'User_profiles',
            },
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='register_place',
            name='id_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.States'),
        ),
        migrations.AddField(
            model_name='people',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Roles'),
        ),
        migrations.AddField(
            model_name='people',
            name='subinstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Subinstitutes'),
        ),
        migrations.AddField(
            model_name='people',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.User_profiles'),
        ),
        migrations.AddField(
            model_name='new_user',
            name='id_subinstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Subinstitutes'),
        ),
        migrations.AddField(
            model_name='new_user',
            name='id_user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.User_profiles'),
        ),
        migrations.AddField(
            model_name='modify_user',
            name='id_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.People'),
        ),
        migrations.AddField(
            model_name='modify_user',
            name='id_subinstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Subinstitutes'),
        ),
        migrations.AddField(
            model_name='modify_place',
            name='id_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.States'),
        ),
        migrations.AddField(
            model_name='modify_place',
            name='id_subinstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Subinstitutes'),
        ),
        migrations.AddField(
            model_name='join_group',
            name='id_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.People'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_join_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Join_Group'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_modify_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Modify_Place'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_modify_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Modify_User'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_new_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.New_User'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_register_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Register_Place'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_remove_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Remove_Document'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_upload_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Upload_Document'),
        ),
        migrations.AddField(
            model_name='campus',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.College'),
        ),
        migrations.AddField(
            model_name='campus',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.States'),
        ),
        migrations.AlterUniqueTogether(
            name='institutes',
            unique_together={('id_institute', 'campus')},
        ),
    ]