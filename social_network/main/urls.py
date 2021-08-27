from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('view_user/<int:user_id>/', view_user, name="view_user"),
    path('message_user/<int:user_id>/', message_user, name="message_user"),
    path('post/<int:post_id>/', view_post, name="view_post"),
    path('logout/', user_logout, name="logout"),
    path('login/', user_login, name="login"),
    path('register/', register, name="register"),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
]

