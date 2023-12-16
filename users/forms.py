import dashboard.models
from django.forms import ModelForm


class MyBusinessForm(ModelForm):
    class Meta:
        model = dashboard.models.businessForm
        exclude = ('timeStamp', 'id')