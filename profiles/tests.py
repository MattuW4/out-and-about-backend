from django.contrib.auth.models import User
from rest_framework import status
from .models import Profile
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """
    def setUp(self):
        matt = User.objects.create_user(username='matt', password='passw')

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_automatically_created_on_creation_of_user(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 1)


class ProfiletDetailViewTests(APITestCase):

    def setUp(self):
        matt = User.objects.create_user(username='matt', password='passw')
        bobby = User.objects.create_user(username='bobby', password='passw')

    def test_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/444/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile(self):
        self.client.login(username='matt', password='passw')
        response = self.client.put('/profiles/1/', {'name': 'fred'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'fred')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_profile(self):
        self.client.login(username='matt', password='passw')
        response = self.client.put('/profiles/2/', {'name': 'matt'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
