# Generated by Django 3.0.2 on 2020-12-12 09:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import reports.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('facility', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Hospital Accounts',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Calls_SMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of Calls/SMS',
                'verbose_name_plural': 'No. Calls/SMS',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientsAttendingSupportGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of Clients Attending Support Groups',
                'verbose_name_plural': 'No. of Clients Attending Support Groups',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientsDocumentedAsLTFU_TransferedOrDied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of clients documented as LTFU , Transferred out or Died',
                'verbose_name_plural': 'No. of clients documented as LTFU , Transferred out or Died',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='hospital_clients_newly_and_uniquely_enrolled_into_mms_care_and_support')),
            ],
            options={
                'verbose_name': "No. of clients newly and uniquely enrolled into MM's care and support",
                'verbose_name_plural': "No. of clients newly and uniquely enrolled into MM's care and support",
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientsTraced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of Clients traced',
                'verbose_name_plural': 'No. of Clients traced',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientsWithRecentViralLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of Clients with recent Viral load',
                'verbose_name_plural': 'No. of Clients with recent Viral load',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientsWithSuppressedViralLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of Clients with suppressed viral load',
                'verbose_name_plural': 'No. of Clients with suppressed viral load',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DBS_Samples_Taken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('six_weeks_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('six_weeks_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('six_weeks_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('six_weeks_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('nine_months_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('nine_months_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('nine_months_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('nine_months_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('eighteen_months_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('eighteen_months_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('eighteen_months_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('eighteen_months_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'DBS Samples taken',
                'verbose_name_plural': 'DBS Samples taken',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HIVPositivesFromIndexTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('male_children_15yrs_above', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15)])),
                ('female_children_15yrs_above', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15)])),
                ('male_partners', models.IntegerField(blank=True, null=True)),
                ('female_partners', models.IntegerField(blank=True, null=True)),
                ('male_relative', models.IntegerField(blank=True, null=True)),
                ('female_relative', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of HIV Positives from index testing',
                'verbose_name_plural': 'No. of HIV Positives from index testing',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='IndexClientContactsTestedForHIV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('male_children_15yrs_above', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15)])),
                ('female_children_15yrs_above', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15)])),
                ('male_partners', models.IntegerField(blank=True, null=True)),
                ('female_partners', models.IntegerField(blank=True, null=True)),
                ('male_relative', models.IntegerField(blank=True, null=True)),
                ('female_relative', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of index client contacts tested for HIV',
                'verbose_name_plural': 'No. of index client contacts tested for HIV',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MMSClientsNewlyInitiatedOnARVs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of clients newly initiated on ARVs',
                'verbose_name_plural': 'No. of clients newly initiated on ARVs',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MMSClientsOnARVs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of MM clients on ARVs',
                'verbose_name_plural': 'No. of MM clients on ARVs',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NumberOfPositiveEID_Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('six_weeks_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('six_weeks_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('six_weeks_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('six_weeks_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('nine_months_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('nine_months_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('nine_months_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('nine_months_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('eighteen_months_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('eighteen_months_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('eighteen_months_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('eighteen_months_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Number of positive EID Result',
                'verbose_name_plural': 'Number of positive EID Result',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ViralLoadTestDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'), ('Week 5', 'Week 5')], max_length=50)),
                ('pregnant_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('pregnant_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('pregnant_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('pregnant_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('feeding_10_to_14', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(10), django.core.validators.MaxValueValidator(14)])),
                ('feeding_15_to_19', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(15), django.core.validators.MaxValueValidator(19)])),
                ('feeding_20_to_24', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(20), django.core.validators.MaxValueValidator(24)])),
                ('feeding_25_or_more', models.IntegerField(blank=True, null=True, validators=[reports.models.MyMinValueValidator(25)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No. of Viral Load done',
                'verbose_name_plural': 'No. of Viral Load done',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MontlyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('calls_sms', models.ManyToManyField(to='reports.Calls_SMS', verbose_name='monthly_report_calls_sms')),
                ('clients_attending_support_groups', models.ManyToManyField(to='reports.ClientsAttendingSupportGroups', verbose_name='monthly_report_clients_attending_support_groups')),
                ('clients_documented_as_ltfu_transfered_or_diend', models.ManyToManyField(to='reports.ClientsDocumentedAsLTFU_TransferedOrDied', verbose_name='monthly_report_clients_documented_as_ltfu_transfered_or_diend')),
                ('clients_newly_and_uniquely_enrolled_into_mms_care_and_support', models.ManyToManyField(to='reports.ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport', verbose_name='monthly_report_clients_newly_and_uniquely_enrolled_into_mms_care_and_support')),
                ('clients_traced', models.ManyToManyField(to='reports.ClientsTraced', verbose_name='monthly_report_clients_traced')),
                ('clients_with_recent_viral_load', models.ManyToManyField(to='reports.ClientsWithRecentViralLoad', verbose_name='monthly_report_clients_with_recent_viral_load')),
                ('clients_with_suppressed_viral_load', models.ManyToManyField(to='reports.ClientsWithSuppressedViralLoad', verbose_name='monthly_report_clients_with_suppressed_viral_load')),
                ('dbs_samples_taken', models.ManyToManyField(to='reports.DBS_Samples_Taken', verbose_name='monthly_report_dbs_samples_taken')),
                ('hiv_positives_from_index_testing', models.ManyToManyField(to='reports.HIVPositivesFromIndexTesting', verbose_name='monthly_report_hiv_positives_from_index_testing')),
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='hospital_monthly_report')),
                ('index_client_contacts_tested_For_hiv', models.ManyToManyField(to='reports.IndexClientContactsTestedForHIV', verbose_name='monthly_report_index_client_contacts_tested_For_hiv')),
                ('mms_client_on_arvs', models.ManyToManyField(to='reports.MMSClientsOnARVs', verbose_name='monthly_report_mms_client_on_arvs')),
                ('mms_clients_newly_initiated_on_arvs', models.ManyToManyField(to='reports.MMSClientsNewlyInitiatedOnARVs', verbose_name='monthly_report_mms_clients_newly_initiated_on_arvs')),
                ('number_of_positive_eid', models.ManyToManyField(to='reports.NumberOfPositiveEID_Results', verbose_name='monthly_reportnumber_of_positive_eid')),
                ('viral_load_test_done', models.ManyToManyField(to='reports.ViralLoadTestDone', verbose_name='monthly_report_viral_load_test_done')),
            ],
        ),
    ]