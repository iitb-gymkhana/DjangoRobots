from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from robots.forms import RuleAdminForm, UrlForm
from robots.models import Rule, Url

# TODO: [Good Practice] Implement a new User model extending the exsiting user model
# TODO: https://realpython.com/manage-users-in-django-admin/


class RuleAdmin(admin.ModelAdmin):
    form = RuleAdminForm
    fieldsets = (
        (None, {'fields': ('robot', 'sites')}),
        (_('URL patterns'), {
            'fields': ('allowed', 'disallowed'),
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('crawl_delay',),
        }),
    )
    list_filter = ('sites',)
    list_display = ('robot', 'allowed_urls', 'disallowed_urls')
    search_fields = ('robot', 'allowed__pattern', 'disallowed__pattern')
    filter_horizontal = ('sites', 'allowed', 'disallowed')


class UrlAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_by')
    # TODO: Add last_updated_on after changing model
    list_filter = ('created_by',)
    form = UrlForm

    def get_form(self, request, *args, **kwargs):
        form = super(UrlAdmin, self).get_form(request, *args, **kwargs)
        form.current_user = request.user
        return form

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Url, UrlAdmin)
admin.site.register(Rule, RuleAdmin)
