from django import forms
from django.contrib.auth.models import User
from monopolyprobability.models import Property, Owned


class OwnedForm(forms.Form):
    property = forms.ModelChoiceField(queryset=Property.objects.filter(owner=None), empty_label='Property Gaining')

    def save(self, force_insert=False, force_update=False, using=None):
        data = self.cleaned_data
        owned = Owned(property=data['property'], user=User.objects.get(pk=1))
        owned.save()
        return owned


class TradeForm(OwnedForm):
    property_losing = forms.ModelChoiceField(queryset=Property.objects.filter(owner=1), empty_label='Property Losing')

    def save(self, force_insert=False, force_update=False, using=None):
        data = self.cleaned_data
        Owned.objects.get(property=data['property_losing']).delete()
        owned = Owned(property=data['property'], user=User.objects.get(pk=1))
        owned.save()
        return owned


class OwnedOtherForm(forms.Form):
    property = forms.ModelChoiceField(queryset=Property.objects.filter(owner=None), empty_label='Someone Else Got It')

    def save(self, force_insert=False, force_update=False, using=None):
        data = self.cleaned_data
        owned = Owned(property=data['property'], user=User.objects.get(pk=2))
        owned.save()
        return owned