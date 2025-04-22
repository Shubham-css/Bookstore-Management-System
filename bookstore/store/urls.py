from django.urls import path
from .views import HomePageView,RegisterView, LoginView, LogoutView  #  Import the CBV from views.py
from .views import AddBookView
from .views import BookListView, BookDetailView
from .views import AddToCartView, CartView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add-book/', AddBookView.as_view(), name='add_book'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('add-to-cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
]
