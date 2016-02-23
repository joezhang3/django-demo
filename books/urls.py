from django.conf.urls import url
from books.views import *

urlpatterns = [
    url(r'^$', welcome),
    url(r'^getData/', getData),
]
