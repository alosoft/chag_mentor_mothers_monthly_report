from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, BaseValidator

# Create your models here.

# date = models.DateField(auto_now=False, auto_now_add=False)


class MyMinValueValidator(BaseValidator):
    message = 'Ensure this value is greater than or equal to %(limit_value)s.'
    code = 'min_value'

    def compare(self, a, b):
        if a == 0:
            return False
        return a < b


class Hospital(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    facility = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Hospital Accounts'

    def __str__(self):
        return self.email

    def get_username(self):
        return self.email


class ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport(models.Model):

    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )
    hospital = models.OneToOneField(
        Hospital, verbose_name="hospital_clients_newly_and_uniquely_enrolled_into_mms_care_and_support", on_delete=models.CASCADE)
    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hospital.name} {self.week}\'s Clients Newly and Uniquely Enrolled into MMS Care and Support'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of clients newly and uniquely enrolled into MM\'s care and support'
        verbose_name_plural = 'No. of clients newly and uniquely enrolled into MM\'s care and support'


class MMSClientsNewlyInitiatedOnARVs(models.Model):

    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s MMS Clients Newly Initiated on ARVs'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of clients newly initiated on ARVs'
        verbose_name_plural = 'No. of clients newly initiated on ARVs'


class MMSClientsOnARVs(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s MMS Clients On ARVs'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of MM clients on ARVs'
        verbose_name_plural = 'No. of MM clients on ARVs'


class IndexClientContactsTestedForHIV(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    male_children_15yrs_above = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(15)])
    female_children_15yrs_above = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(15)])
    male_partners = models.IntegerField(null=True, blank=True)
    female_partners = models.IntegerField(null=True, blank=True)
    male_relative = models.IntegerField(null=True, blank=True)
    female_relative = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Index Clients Contacts Tested for HIV'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of index client contacts tested for HIV'
        verbose_name_plural = 'No. of index client contacts tested for HIV'


class HIVPositivesFromIndexTesting(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    male_children_15yrs_above = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(15)])
    female_children_15yrs_above = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(15)])
    male_partners = models.IntegerField(null=True, blank=True)
    female_partners = models.IntegerField(null=True, blank=True)
    male_relative = models.IntegerField(null=True, blank=True)
    female_relative = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s HIV Positives from Index Testing'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of HIV Positives from index testing'
        verbose_name_plural = 'No. of HIV Positives from index testing'


class ClientsAttendingSupportGroups(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Clients attending Support Groups'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of Clients Attending Support Groups'
        verbose_name_plural = 'No. of Clients Attending Support Groups'


class ClientsWithRecentViralLoad(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Clients with recent Viral Load'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of Clients with recent Viral load'
        verbose_name_plural = 'No. of Clients with recent Viral load'


class ClientsWithSuppressedViralLoad(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Clients with suppressed Viral load'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of Clients with suppressed viral load'
        verbose_name_plural = 'No. of Clients with suppressed viral load'


class ViralLoadTestDone(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Viral Load Test done'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of Viral Load done'
        verbose_name_plural = 'No. of Viral Load done'


class ClientsDocumentedAsLTFU_TransferedOrDied(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Clients documented as LTFU, Transfered out or Died'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of clients documented as LTFU , Transferred out or Died'
        verbose_name_plural = 'No. of clients documented as LTFU , Transferred out or Died'


class ClientsTraced(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Clients Traced'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of Clients traced'
        verbose_name_plural = 'No. of Clients traced'


class Calls_SMS(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    pregnant_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(10), MaxValueValidator(14)])
    pregnant_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(15), MaxValueValidator(19)])
    pregnant_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                            MyMinValueValidator(20), MaxValueValidator(24)])
    pregnant_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    feeding_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(10), MaxValueValidator(14)])
    feeding_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(15), MaxValueValidator(19)])
    feeding_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                           MyMinValueValidator(20), MaxValueValidator(24)])
    feeding_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Calls or SMS'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'No. of Calls/SMS'
        verbose_name_plural = 'No. Calls/SMS'


class DBS_Samples_Taken(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    six_weeks_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                             MyMinValueValidator(10), MaxValueValidator(14)])
    six_weeks_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                             MyMinValueValidator(15), MaxValueValidator(19)])
    six_weeks_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                             MyMinValueValidator(20), MaxValueValidator(24)])
    six_weeks_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    nine_months_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                               MyMinValueValidator(10), MaxValueValidator(14)])
    nine_months_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                               MyMinValueValidator(15), MaxValueValidator(19)])
    nine_months_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                               MyMinValueValidator(20), MaxValueValidator(24)])
    nine_months_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    eighteen_months_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                                   MyMinValueValidator(10), MaxValueValidator(14)])
    eighteen_months_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                                   MyMinValueValidator(15), MaxValueValidator(19)])
    eighteen_months_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                                   MyMinValueValidator(20), MaxValueValidator(24)])
    eighteen_months_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s DBS Samples taken'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'DBS Samples taken'
        verbose_name_plural = 'DBS Samples taken'


class NumberOfPositiveEID_Results(models.Model):
    weeks = (
        ('Week 1', 'Week 1'),
        ('Week 2', 'Week 2'),
        ('Week 3', 'Week 3'),
        ('Week 4', 'Week 4'),
        ('Week 5', 'Week 5')
    )

    week = models.CharField(choices=weeks, max_length=50)
    six_weeks_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                             MyMinValueValidator(10), MaxValueValidator(14)])
    six_weeks_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                             MyMinValueValidator(15), MaxValueValidator(19)])
    six_weeks_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                             MyMinValueValidator(20), MaxValueValidator(24)])
    six_weeks_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    nine_months_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                               MyMinValueValidator(10), MaxValueValidator(14)])
    nine_months_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                               MyMinValueValidator(15), MaxValueValidator(19)])
    nine_months_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                               MyMinValueValidator(20), MaxValueValidator(24)])
    nine_months_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])
    eighteen_months_10_to_14 = models.IntegerField(null=True, blank=True, validators=[
                                                   MyMinValueValidator(10), MaxValueValidator(14)])
    eighteen_months_15_to_19 = models.IntegerField(null=True, blank=True, validators=[
                                                   MyMinValueValidator(15), MaxValueValidator(19)])
    eighteen_months_20_to_24 = models.IntegerField(null=True, blank=True, validators=[
                                                   MyMinValueValidator(20), MaxValueValidator(24)])
    eighteen_months_25_or_more = models.IntegerField(
        null=True, blank=True, validators=[MyMinValueValidator(25)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week}\'s Number of Positive EID Results'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Number of positive EID Result'
        verbose_name_plural = 'Number of positive EID Result'


class MonthlyReport(models.Model):
    hospital = models.OneToOneField(
        Hospital, verbose_name="hospital_monthly_report", on_delete=models.CASCADE)
    clients_newly_and_uniquely_enrolled_into_mms_care_and_support = models.ManyToManyField(
        ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport, verbose_name="monthly_report_clients_newly_and_uniquely_enrolled_into_mms_care_and_support")
    mms_clients_newly_initiated_on_arvs = models.ManyToManyField(
        MMSClientsNewlyInitiatedOnARVs, verbose_name="monthly_report_mms_clients_newly_initiated_on_arvs")
    mms_client_on_arvs = models.ManyToManyField(
        MMSClientsOnARVs, verbose_name="monthly_report_mms_client_on_arvs")
    index_client_contacts_tested_For_hiv = models.ManyToManyField(
        IndexClientContactsTestedForHIV, verbose_name="monthly_report_index_client_contacts_tested_For_hiv")
    hiv_positives_from_index_testing = models.ManyToManyField(
        HIVPositivesFromIndexTesting, verbose_name="monthly_report_hiv_positives_from_index_testing")
    clients_attending_support_groups = models.ManyToManyField(
        ClientsAttendingSupportGroups, verbose_name="monthly_report_clients_attending_support_groups")
    clients_with_recent_viral_load = models.ManyToManyField(
        ClientsWithRecentViralLoad, verbose_name="monthly_report_clients_with_recent_viral_load")
    clients_with_suppressed_viral_load = models.ManyToManyField(
        ClientsWithSuppressedViralLoad, verbose_name="monthly_report_clients_with_suppressed_viral_load")
    viral_load_test_done = models.ManyToManyField(
        ViralLoadTestDone, verbose_name="monthly_report_viral_load_test_done")
    clients_documented_as_ltfu_transfered_or_diend = models.ManyToManyField(
        ClientsDocumentedAsLTFU_TransferedOrDied, verbose_name="monthly_report_clients_documented_as_ltfu_transfered_or_diend")
    clients_traced = models.ManyToManyField(
        ClientsTraced, verbose_name="monthly_report_clients_traced")
    calls_sms = models.ManyToManyField(
        Calls_SMS, verbose_name="monthly_report_calls_sms")
    dbs_samples_taken = models.ManyToManyField(
        DBS_Samples_Taken, verbose_name="monthly_report_dbs_samples_taken")
    number_of_positive_eid = models.ManyToManyField(
        NumberOfPositiveEID_Results, verbose_name="monthly_reportnumber_of_positive_eid")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Monthly Report of {self.hospital.name} - {self.created}'
