from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
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


class URLForm(forms.ModelForm):
    # TODO: Check if user is superuser to allow for changes

    # TODO: Add default as user.username
    reverse_proxy_initial = forms.CharField(
        disabled=True,  max_length=20, label="Initial", initial='/')

    class Meta:
        model = Url
        exclude = ('created_by',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        # Should actually be set while rendering for the first time and not while saving. Solve the previous TODO
        form.instance.reverse_proxy_initial = self.request.user.username
        return super().form_valid(form)
