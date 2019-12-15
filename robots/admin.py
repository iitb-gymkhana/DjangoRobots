from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from robots.forms import RuleAdminForm, URLForm
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


class URLAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_by')
    # TODO: Add last_updated_on after changing model
    list_filter = ('created_by',)

    form = URLForm


admin.site.register(Url, URLAdmin)
admin.site.register(Rule, RuleAdmin)
