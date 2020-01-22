from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from robots.models import Url
from django.contrib.auth import get_user_model


class UrlModelTestCase(TestCase):
    def test_save_object_to_DB(self):
        user1 = User.objects.create_user(username='user1')
        # creates multiple objects directly in database
        Url1 = Url.objects.create(
            created_by=user1, reverse_proxy_initial="/~user1", pattern="hello1/")
        self.assertNotEqual(str(Url1), 'hello1/')
        self.assertEqual(str(Url1), '/~user1/hello1/')

        Url2 = Url.objects.create(
            created_by=user1, reverse_proxy_initial="/~user1", pattern="/hello2/")
        self.assertEqual(str(Url2), '/~user1/hello2/')

        Url3 = Url.objects.create(created_by=user1, pattern="~user1/hello3/")
        self.assertEqual(str(Url3), '/~user1/hello3/')

        Url4 = Url.objects.create(created_by=user1, pattern="/~user1/hello4/")
        self.assertEqual(str(Url4), '/~user1/hello4/')


class RuleModelTestCase(TestCase):
    pass
