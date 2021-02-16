from django.urls import path

from . import views

app_name = 'BOT'
urlpatterns = [
    path('', views.index, name='index'),
    path('board', views.board, name='board'),
    path('bot',views.bot, name='bot'),
]
