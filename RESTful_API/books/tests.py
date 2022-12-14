from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Books

from django.urls import reverse

class BookTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="admin", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="admin2", password="pass"
        )
        testuser2.save()

        test_book = Books.objects.create(
            name_book="rake",
            owner=testuser1,
            description="historical Book",
        )
        test_book.save()


    def setUp(self):
        self.client.login(username='admin', password="pass")




    def test_books_model(self):
        book = Books.objects.get(id=1)
        actual_owner = str(book.owner)
        actual_name = str(book.name_book)
        actual_description = str(book.description)
        self.assertEqual(actual_owner, "admin")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "historical Book"
        )

    def test_get_book_list(self):
        url = reverse("Book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(len(books), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("Book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("Book_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)