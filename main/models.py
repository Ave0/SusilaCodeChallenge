from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import DateTimeField


class Contact(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=25)
    address = models.TextField()
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    count = models.PositiveIntegerField()
    subscription_cost = models.PositiveIntegerField()
    topic = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='books')
    def __str__(self):
        return self.title


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    #We could use this if we have the option to use external librarys
    #phone = models.PhoneNumberField(null=True, blank=True)
    phone = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    subscriber = models.ForeignKey(Subscriber,  on_delete=models.CASCADE, related_name='subscriber')
    book  = models.ForeignKey(Book,  on_delete=models.CASCADE, related_name='book')
    borrowed_date = models.DateField(auto_now=True)
    amount_paid = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    returned = models.BooleanField(default = False)
    def __str__(self):
        return self.subscriber.user.username