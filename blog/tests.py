from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from .views import home
from .models import Comics

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.comics = [
            Comics.objects.create(title='Spiderman'),
            Comics.objects.create(title='Superman'),
            Comics.objects.create(title='Batman'),
        ]

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertEqual(len(response.context['page_obj']), 3)
        self.assertEqual(response.context['page_obj'][0].title, 'Batman')
        self.assertEqual(response.context['page_obj'][1].title, 'Spiderman')
        self.assertEqual(response.context['page_obj'][2].title, 'Superman')

    def test_home_view_pagination(self):
        url = reverse('home')
        response = self.client.get(url, {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertEqual(len(response.context['page_obj']), 3)
        self.assertEqual(response.context['page_obj'][0].title, 'Batman')
