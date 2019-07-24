from rest_framework import serializers
from .models import Author, Book, Subscriber, Subscription, Contact
from django.contrib.auth.models import User



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id','username','first_name','email','surname']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ['name','address']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title','description','count','subscription_cost','topic', 'author')

class Book2Serializer(serializers.Serializer):
    costo = serializers.FloatField()
    
    class Meta:
        fields = ('costo',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['user','address','phone']

class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ['subscriber','book','borrowed_date','amount_paid','days','returned']

class Subscription2Serializer(serializers.HyperlinkedModelSerializer):
    due_amount = serializers.FloatField()
    class Meta:
        model = Subscription
        fields = ['subscriber','book','borrowed_date','amount_paid','days','returned','due_amount']

class Subscription3Serializer(serializers.Serializer):
    username = serializers.CharField()
    class Meta:
        model = Subscription
        fields = ['username']



