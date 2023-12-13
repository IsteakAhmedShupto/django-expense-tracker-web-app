from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='welcome'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('logout', views.logout_view, name='logout'),
    path('show_books', views.show_books, name='show_books'),
    path('show_books/<int:id>', views.book, name='book'),
    path('show_books/<int:id>/edit', views.book_edit,
         name='book_edit'),
    path('show_books/<int:id>/delete', views.book_delete,
         name='book_delete'),
    path('add_book', views.add_book, name='add_book')
]
