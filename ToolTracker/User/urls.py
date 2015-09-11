__author__ = 'ishant'

from django.conf.urls import url


from . import views

urlpatterns = [
    # ex: /polls/

    # ex: /polls/5/
    url(r"^$",views.index,name="index"),
]


