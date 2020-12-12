from django.contrib import admin
from reports import models
# Register your models here.

admin.site.register(models.ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport)
admin.site.register(models.MMSClientsNewlyInitiatedOnARVs)
admin.site.register(models.MMSClientsOnARVs)
admin.site.register(models.IndexClientContactsTestedForHIV)
admin.site.register(models.HIVPositivesFromIndexTesting)
admin.site.register(models.ClientsAttendingSupportGroups)
admin.site.register(models.ClientsWithRecentViralLoad)
admin.site.register(models.ClientsWithSuppressedViralLoad)
admin.site.register(models.ViralLoadTestDone)
admin.site.register(models.ClientsDocumentedAsLTFU_TransferedOrDied)
admin.site.register(models.ClientsTraced)
admin.site.register(models.Calls_SMS)
admin.site.register(models.DBS_Samples_Taken)
admin.site.register(models.NumberOfPositiveEID_Results)

admin.site.register(models.MonthlyReport)
admin.site.register(models.Hospital)
