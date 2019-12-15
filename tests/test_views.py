# -*- coding: utf-8 -*-

from django.contrib.auth.models import AnonymousUser, User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.encoding import force_text

from robots.models import Rule, Url
from robots.views import RuleList

from .base import BaseTest


class ViewTest(BaseTest):

    def setUp(self):
        super(BaseTest, self).setUp()
        usr1 = User.objects.create_user(username="usr1")
        usr2 = User.objects.create_user(username="usr2")
        site_1 = Site.objects.get(domain='example.com')
        site_2 = Site.objects.create(domain='https://sub.example.com')

        url_admin = Url.objects.create(
            pattern='/admin', created_by=usr1)
        url_root = Url.objects.create(
            pattern='/', created_by=usr2)
        url_media = Url.objects.create(
            pattern='/media', created_by=usr1)

        rule_all = Rule.objects.create(robot='*', crawl_delay=10)
        rule_1 = Rule.objects.create(robot='Bing', crawl_delay=20)
        rule_2 = Rule.objects.create(robot='Googlebot')

        rule_all.allowed.add(url_root)
        for url in [url_admin, url_media]:
            rule_all.disallowed.add(url)
        for site in [site_1, site_2]:
            rule_all.sites.add(site)

        rule_1.allowed.add(url_root)
        rule_1.disallowed.add(url_admin)
        rule_1.sites.add(site_1)

        rule_2.disallowed.add(url_media)
        rule_2.sites.add(site_2)

    def _test_stanzas(self, stanzas):
        for stanza in stanzas:
            if stanza.startswith('User-agent: *'):
                self.assertTrue('Allow: /' in stanza)
                self.assertTrue('Disallow: /admin' in stanza)
                self.assertTrue('Disallow: /media' in stanza)
                self.assertTrue('Crawl-delay: 10' in stanza)
            elif stanza.startswith('User-agent: Bing'):
                self.assertTrue('Allow: /' in stanza)
                self.assertTrue('Disallow: /admin' in stanza)
                self.assertFalse('Disallow: /media' in stanza)
                self.assertFalse('Crawl-delay: 10' in stanza)
                self.assertTrue('Crawl-delay: 20' in stanza)
            elif stanza.startswith('User-agent: Googlebot'):
                self.assertFalse('Allow: /' in stanza)
                self.assertFalse('Disallow: /admin' in stanza)
                self.assertTrue('Disallow: /media' in stanza)
                self.assertFalse('Crawl-delay: 10' in stanza)
                self.assertFalse('Crawl-delay: 20' in stanza)
                self.assertFalse('Crawl-delay' in stanza)

    def test_view_site_1(self):
        request = self.get_request(
            path='/', user=AnonymousUser(), lang='en')

        view_obj = RuleList()
        view_obj.request = request
        view_obj.current_site = view_obj.get_current_site(request)
        view_obj.object_list = view_obj.get_queryset()
        context = view_obj.get_context_data(object_list=view_obj.object_list)
        self.assertEqual(context['object_list'].count(), 2)
        self.assertTrue(context['object_list'].filter(robot='*').exists())
        self.assertTrue(context['object_list'].filter(robot='Bing').exists())

        response = view_obj.render_to_response(context)
        response.render()
        content = force_text(response.content)
        print(content)
        # if settings.ROBOTS_USE_SITEMAP:
        self.assertTrue(
            'Sitemap: http://example.com/sitemap.xml' in content)
        stanzas = content.split('\n\n')
        self._test_stanzas(stanzas)

    def test_view_site_2(self):
        request = self.get_request(
            path='/', user=AnonymousUser(), lang='en')

        view_obj = RuleList()
        view_obj.request = request
        view_obj.current_site = Site.objects.get(pk=2)
        view_obj.object_list = view_obj.get_queryset()
        context = view_obj.get_context_data(object_list=view_obj.object_list)
        self.assertEqual(context['object_list'].count(), 2)
        self.assertTrue(context['object_list'].filter(robot='*').exists())
        self.assertTrue(context['object_list'].filter(
            robot='Googlebot').exists())

        response = view_obj.render_to_response(context)
        response.render()
        content = force_text(response.content)
        # if settings.ROBOTS_USE_SITEMAP:
        self.assertTrue(
            'Sitemap: https://sub.example.com/sitemap.xml' in content)
        self.assertTrue('Host: https://sub.example.com' in content)
        stanzas = content.split('\n\n')
        self._test_stanzas(stanzas)

    def test_use_scheme_in_host_setting(self):
        request = self.get_request(
            path='/', user=AnonymousUser(), lang='en')

        view_obj = RuleList()
        view_obj.request = request
        view_obj.current_site = Site.objects.get(pk=1)
        view_obj.object_list = view_obj.get_queryset()

        with self.settings(ROBOTS_USE_HOST=True):
            with self.settings(ROBOTS_USE_SCHEME_IN_HOST=True):
                context = view_obj.get_context_data(
                    object_list=view_obj.object_list)
                response = view_obj.render_to_response(context)
                response.render()
                content = force_text(response.content)
                self.assertTrue('Host: http://example.com' in content)
            with self.settings(ROBOTS_USE_SCHEME_IN_HOST=False):
                context = view_obj.get_context_data(
                    object_list=view_obj.object_list)
                response = view_obj.render_to_response(context)
                response.render()
                content = force_text(response.content)
                self.assertTrue('Host: example.com' in content)

        with self.settings(ROBOTS_USE_HOST=False):
            context = view_obj.get_context_data(
                object_list=view_obj.object_list)
            response = view_obj.render_to_response(context)
            response.render()
            content = force_text(response.content)
            self.assertFalse('Host: example.com' in content)

    def test_cached_sitemap(self):
        request = self.get_request(path='/', user=AnonymousUser(), lang='en')

        view_obj = RuleList()
        view_obj.request = request
        view_obj.current_site = Site.objects.get(pk=1)
        view_obj.object_list = view_obj.get_queryset()
        context = view_obj.get_context_data(object_list=view_obj.object_list)
        response = view_obj.render_to_response(context)
        response.render()
        content = force_text(response.content)
        # if settings.ROBOTS_USE_SITEMAP:
        self.assertTrue(
            'Sitemap: http://example.com/sitemap.xml' in content)

        with self.settings(ROBOTS_SITEMAP_VIEW_NAME='cached-sitemap'):
            context = view_obj.get_context_data(
                object_list=view_obj.object_list)
            response = view_obj.render_to_response(context)
            response.render()
            content = force_text(response.content)
        # if settings.ROBOTS_USE_SITEMAP:
        self.assertTrue(
            'Sitemap: http://example.com/other/sitemap.xml' in content)
