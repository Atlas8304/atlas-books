from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from books.models import Book, Author, Genre
from users.models import UserReadingList

class UsersTestCase(TestCase):
    def setUp(self):
        # Initialise a Test User
        self.user = User.objects.create_user('test', 'test@email.com', 'testtest')

        # Initialise some Test Authors
        self.author1 = Author.objects.create(
            first_name="Joe", last_name="Bloggs", age=28, biography="Test Author No1"
        )
        self.author2 = Author.objects.create(
            first_name="Mary", last_name="Bloggs", age=34, biography="Test Author No2"
        )
        self.author3 = Author.objects.create(
            first_name="Kyle", last_name="Ackerman", age=45, biography="Test Author No3"
        )

        # Initialise some Test Genres
        self.genre1 = Genre.objects.create(name="Fiction")
        self.genre2 = Genre.objects.create(name="Comedy")
        self.genre3 = Genre.objects.create(name="Horror")

        # Initialise some Test Books
        self.book1 = Book.objects.create(
            title="Book1",
            isbn="123-12345-1234",
            description="Description1",
        )
        self.book2 = Book.objects.create(
            title="Book2",
            isbn="123-54321-1234",
            description="Description2",
        )
        self.book3 = Book.objects.create(
            title="Book3",
            isbn="321-12345-1234",
            description="Description3",
        )

    def test_my_books_list_no_user(self):
        response = self.client.get(reverse("users:mylist"))
        self.assertEqual(response.status_code, 302)

    def test_my_books_list_no_books_selected(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users:mylist"))

        for book in [self.book1, self.book2, self.book3]:
            self.assertNotContains(response, book.title)

    def test_my_books_list(self):
        self.client.force_login(self.user)

        reading_list = UserReadingList.objects.create(user=self.user)
        reading_list.books.add(self.book1)

        response = self.client.get(reverse("users:mylist"))
        
        self.assertContains(response, self.book1.title)
        self.assertNotContains(response, self.book2.title)
        self.assertNotContains(response, self.book3.title)
