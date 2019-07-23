
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Author, Book, Subscriber, Subscription
from django.contrib.auth.models import User
import datetime



class BaseViewTest(APITestCase):
    client = APIClient()


    @staticmethod
    def create_authors(name,address):
        Author.objects.create(name=name, address=address)
    
    @staticmethod
    def create_books(title, description, count, subscription_cost, topic, author):
        Book.objects.create(tittle=title, description=description, count=count,
                            subscription_cost=subscription_cost, topic=topic, author=author)

    @staticmethod
    def create_Subscriber(user,address,phone):
        Subscriber.objects.create(user,address,phone)
    
    @staticmethod
    def create_subscription(subscriber, book, borrowed_date, amount_paid, days, returned):
        Subscription.objects.create(subscriber=subscriber, book=book, borrowed_date=borrowed_date,
                                    amount_paid=amount_paid, days=days, returned=returned)
    

    def setUp(self):
        # add user test data
        user1 = User.objects.create_user("UserTest1", password='123456')
        user2 = User.objects.create_user("UserTest2", password='123456')
        user3 = User.objects.create_user("UserTest3", password='123456')

        # add author test data
        author1 = self.create_authors("Isaac Asimov", "Heaven #132, Cool district" )
        author2 = self.create_authors("Arthur C. Clark", "Heaven #102, Smooth district" )
        author3 = self.create_authors("Fake person", "Fake street #2 False district")

        # add books test data
        book1 = self.create_books("Title Example 1", "Description example 1", 1, 10, "Science Fiction", author1 )
        book2 = self.create_books("Title Example 2", "Description example 2", 2, 11, "Science Fiction", author2 )
        book3 = self.create_books("Title Example 3", "Description example 3", 3, 12, "Biology", author2,author1 )
        book4 = self.create_books("Title Example 4", "Description example 4", 4, 13, "Science", author3 )

        # add Subscriber test data
        suscriber1 = self.create_suscriber(user1, "This is my address 1", "4421756845" )
        suscriber2 = self.create_suscriber(user2, "This is my address 2", "5504985579" )
        suscriber3 = self.create_suscriber(user3, "This is my address 3", "6681598761" )

        # add Subscription test data
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 45 , 12 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 46 , 13 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 48 , 14 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 5 , 11 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 55 , 9 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 14 , 11 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 24 , 85 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 50 , 23 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 12 , 41 , True )
        self.create_subscription(suscriber1, book1, datetime.datetime.now() , 9 , 87 , True )

        
        
        

        



class GetAllBooks(BaseViewTest):

    def test_get_all_books(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Book.objects.all()
        serialized = BookSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
