from django.conf.urls import url
from django.contrib import admin
from django.urls.conf import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register('books',views.CRUDBooksView)
router.register('author',views.CRUDAuthorView)
router.register('subscriber',views.CRUDSubscriberView)
router.register('subscription',views.CRUDSubscriptionView)
router.register('user',views.CRUDUserView)


urlpatterns = [
  url(r'^admin/', admin.site.urls),
  #url('api-auth/', include('rest_framework.urls')),
  path('', include(router.urls)),
  url('book-author/', views.BookFilterView.as_view(), name="books-filter"),
  url('subscription-amount/', views.SubscriptionAmount.as_view(), name="subscription-filter"),
  url('subscription-expired/', views.SubscriberDebt.as_view(), name="subscription-filter"),
  #url('test/', views.SubscriberDebt.as_view(), name="test-view"),
  #url('testplain/', views.PlainTest, name="test-view"),


]
