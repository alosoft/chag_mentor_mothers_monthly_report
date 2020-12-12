from reports.models import ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport
from django import forms


class ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupportForm(forms.ModelForm):

    class Meta:
        model = ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupport
        fields = ('hospital', 'week', 'pregnant_10_to_14', 'pregnant_15_to_19',
                  'pregnant_20_to_24', 'pregnant_25_or_more', 'feeding_10_to_14', 'feeding_15_to_19', 'feeding_20_to_24', 'feeding_25_or_more')
        exclude = ('',)
