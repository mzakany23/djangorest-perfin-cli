from django.conf.urls import patterns, include, url
from django.contrib import admin

# app
from api.transaction.views import (
	TransactionsViewSet,
	UploadTransactionsViewSet,
	AllTransactionsViewSet,
	FilterByWordListViewSet,
	FilterByAmountsViewSet)

from api.riot_api.views import RIOTAPITransactions

from home.views import HomeView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# api
urlpatterns += patterns('api.views',
	url(r'^api/transactions/(?P<slug>[-\w]+)/$',TransactionsViewSet.as_view()),
	url(r'^api/transactions/$',AllTransactionsViewSet.as_view()),
	url(r'^api/upload-transactions/(?P<slug>[-\w]+)/$',UploadTransactionsViewSet.as_view()),
	url(r'^api/search-by-wordlist/$',FilterByWordListViewSet.as_view()),
	url(r'^api/search-by-amounts/$',FilterByAmountsViewSet.as_view()),

)

urlpatterns += patterns('home.views',
	url(r'^$',HomeView.as_view()),
)

urlpatterns += patterns('api.riot_api.views',
	url(r'^riot/transactions/(?P<slug>[-\w]+)/$',RIOTAPITransactions.as_view()),
)