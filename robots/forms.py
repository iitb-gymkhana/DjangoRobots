from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from robots.models import Rule, Url


class RuleAdminForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = "__all__"

    def clean(self):
        if (not self.cleaned_data.get("disallowed", False) and
                not self.cleaned_data.get("allowed", False)):
            raise forms.ValidationError(
                _('Please specify at least one allowed or dissallowed URL.'))
        return self.cleaned_data


class UrlForm(forms.ModelForm):
    # TODO: Any Chance to use forms.MultiValueField with initial input of "/user"?
    # TODO: Add a custom validation for URLs

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['reverse_proxy_initial'].initial = self.current_user.userprofile.proxy
        if not self.current_user.is_superuser:
            self.fields['reverse_proxy_initial'].disabled = True

    reverse_proxy_initial = forms.CharField(
        max_length=20, label='Initial')

    class Meta:
        model = Url
        exclude = ('created_by',)
