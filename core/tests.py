class UserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='user1', email='nautatva@iitb.ac.in', password='foo', proxy='/user1')
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'nautatva@iitb.ac.in')
        self.assertEqual(user.proxy, '/user1')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            'admin1', 'nautatva@iitb.ac.in', 'foo', 'all')
        self.assertEqual(admin_user.username, 'admin1')
        self.assertEqual(admin_user.email, 'nautatva@iitb.ac.in')
        self.assertEqual(admin_user.proxy, 'all')

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='admin2', email='nautatva@iitb.ac.in', password='foo', proxy='all', is_superuser=False)
