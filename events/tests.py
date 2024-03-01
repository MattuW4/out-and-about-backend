from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Event



class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """
    def setUp(self):
        User.objects.create_user(username='matt', password='passw')
        
    def test_can_list_events(self):
        
        adam = User.objects.get(username='matt')
        Event.objects.create(owner=adam, title='a title', event_date='2024-12-12')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
        
    def test_logged_in_user_can_create_event(self):
        self.client.login(username='matt', password='passw')
        response = self.client.post('/events/', {'title': 'a title', 'event_date': '2024-12-12'})
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_event(self):
        response = self.client.post('/events/', {'title': 'a title', 'event_date': '2024-12-12'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Event.objects.count()
        self.assertEqual(count, 0)
        
class EventDetailViewTests(APITestCase):
    """
    Tests for event model detail view
    """
    def setUp(self):
        matt = User.objects.create_user(username='matt', password='passw')
        kaitlin = User.objects.create_user(username='kaitlin', password='passw')
        Event.objects.create(
            owner=matt, 
            title='a title', 
            description='matts content',
            event_date='2024-12-12'
        )
        Event.objects.create(
            owner=kaitlin, 
            title='some other title', 
            description='kaitlins content',
            event_date='2024-12-12'
        )
        
    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/events/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get('/events/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='matt', password='passw')
        response = self.client.put('/events/1/', {'title': 'a new title', 'event_date': '2024-12-12'})
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(event.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_user_cant_update_someone_elses_event(self):
        self.client.login(username='bobby', password='passw')
        response = self.client.put('/events/2/', {'title': 'an edited title', 'event_date': '2024-12-12'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


