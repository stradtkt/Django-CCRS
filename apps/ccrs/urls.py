from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login-page$', views.login_page),
    url(r'^register-page$', views.register_page),
    url(r'^about$', views.about),
    url(r'^reviews$', views.reviews),
    url(r'^services$', views.services),
    url(r'^contact$', views.contact),
    url(r'^review$', views.review),
    url(r'^(?P<id>\d+)/profile$', views.profile),
    url(r'^appointments$', views.appointments),
]