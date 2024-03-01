from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Event



class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')
        
    def test_can_list_events(self):
        
        adam = User.objects.get(username='adam')
        Event.objects.create(owner=adam, title='a title', event_date='2024-12-12')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
        
    def test_logged_in_user_can_create_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/events/', {'title': 'a title', 'event_date': '2024-12-12'})
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_event(self):
        response = self.client.post('/events/', {'title': 'a title', 'event_date': '2024-12-12'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Event.objects.count()
        self.assertEqual(count, 0)
