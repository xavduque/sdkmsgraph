# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from django.urls import path

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('calendar', views.calendar, name='calendar'),
  path('callback', views.callback, name='callback'),
  path('calendar/new', views.newevent, name='newevent'),
  path('users', views.users, name='users'),
  path('user_create', views.new_user, name='user_create'),
]
