
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='index'),  # This is the home page
    path('library/', views.list_books, name="list_books"),
    path('book/create/', views.create_book, name='create_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('genders/', views.list_gender, name="genders"),
    path('genders/create/', views.create_gender, name='create_gender'),
    path('genders/edit/<int:gender_id>/', views.edit_gender, name='edit_gender'),
    path('genders/delete/<int:gender_id>/', views.delete_gender, name='delete_gender'),
]