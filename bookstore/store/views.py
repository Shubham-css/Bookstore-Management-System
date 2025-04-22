from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.

class HomePageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            message = f"<h1>Welcome {request.user.username}!</h1><p><a href='/logout/'>Logout</a></p>"
        else:
            message = "<h1>Welcome to the Bookstore!</h1><p><a href='/login/'>Login</a> | <a href='/register/'>Register</a></p>"

        return HttpResponse(message)

class RegisterView(View):
    def get(self, request):
        return render(request, 'store/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'store/register.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, 'store/register.html', {'error': "Username already taken."})

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('home')
    
class LoginView(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials.'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class AddBookView(LoginRequiredMixin, View):
    @method_decorator(csrf_protect)
    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponse("Unauthorized", status=401)
        return render(request, 'store/add_book.html')

    @method_decorator(csrf_protect)
    def post(self, request):
        if not request.user.is_superuser:
            return HttpResponse("Unauthorized", status=401)

        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description')
        inventory = request.POST.get('inventory')

        if title and author and price and description and inventory:
            Book.objects.create(
                title=title,
                author=author,
                price=price,
                description=description,
                inventory=inventory
            )
            return redirect('home')
        else:
            return render(request, 'store/add_book.html', {'error': 'All fields are required.'})

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'store/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return HttpResponse("Book not found", status=404)
        return render(request, 'store/book_detail.html', {'book': book})

class AddToCartView(View):
    def post(self, request, book_id):
        cart = request.session.get('cart', {})
        cart[str(book_id)] = cart.get(str(book_id), 0) + 1  # Increment quantity
        request.session['cart'] = cart
        return redirect('/cart/')

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = []
        total = 0

        for book_id, quantity in cart.items():
            try:
                book = Book.objects.get(id=book_id)
                book.quantity = quantity
                book.total_price = quantity * book.price
                total += book.total_price
                books.append(book)
            except Book.DoesNotExist:
                pass

        return render(request, 'store/cart.html', {'books': books, 'total': total})
