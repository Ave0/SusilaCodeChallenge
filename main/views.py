from django.shortcuts import render
from .models import Author, Book, Subscriber, Subscription, Contact, User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F, DateTimeField, IntegerField
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AuthorSerializer, UserSerializer, SubscriberSerializer, SubscriptionSerializer, Subscription2Serializer, ContactSerializer, Book2Serializer
from django.db.models import Q, Count, Avg, Sum
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def testview(request):
    return render(request, 'main/index2.html')



class CRUDBooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CRUDAuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CRUDSubscriberView(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class CRUDSubscriptionView(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    #To prevent a subscription if there is no book available.
    def perform_create(self, serializer):
        book_id = self.request.POST['book'].split('/')[-2]
        book_count = Book.objects.filter(id=book_id).values('count')[0]['count']
        book_noreturn = len(Subscription.objects.filter(book=book_id,returned=False))
        book_available = book_count-book_noreturn
        if book_available>0:
            serializer.save()


        

class CRUDUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class BookFilterView(ListAPIView):
    model = Book
    serializer_class = BookSerializer
    #For a url like this : http://127.0.0.1:8000/book-author2/?title=Book1
    def get_queryset(self,*args,**kwargs):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        topic = self.request.query_params.get('topic')
        if title:
            queryset = Book.objects.filter(title=title, count__gte=1)
        if author:
            queryset = Book.objects.filter(author__id=author)
        if topic: 
            print("i enter and the title is =",topic)
            queryset = Book.objects.filter(topic__iexact=topic)

        return queryset


#View for point d)
class SubscriptionAmount(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = Subscription2Serializer
    def get_queryset(self):
        queryset = Subscription.objects.all().annotate(
            due_amount=Sum(F('book__subscription_cost')*F('days')-F('amount_paid')))
        return queryset

#it wont work with sqlite since date/time will store as text
class SubscriberDebt(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = Subscription2Serializer
    def get_queryset(self):
        today = datetime.now()
        queryset = Subscription.objects.all().annotate(
            dayspass=Sum(today-F('borrowed_date'),output_field=DateTimeField())
            ).filter(days__lt=F('dayspass'),returned=False).values('subscriber.user.username')
        print(queryset[0])
        return queryset
