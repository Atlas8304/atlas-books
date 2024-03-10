from django.test import TestCase
from django.urls import reverse

from books.models import Book, Author, Genre


class BooksTestCase(TestCase):
    def setUp(self):
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

    def test_books_list(self):
        response = self.client.get(reverse("books:list") + "?page_size=2")

        for book in [self.book1, self.book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, self.book3.title)

        response = self.client.get(reverse("books:list") + "?page=2&page_size=2")

        self.assertContains(response, self.book3.title)

    def test_detail_page(self):
        response = self.client.get(reverse("books:detail", kwargs={"id": self.book1.id}))

        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.description)
