from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import redirect, render
from .models import AddBook


def index(request):
    return render(request, 'expenses/welcome.html', {})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('show_books')

    form = None

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()

    return render(request, 'expenses/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('show_books')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show_books')
        else:
            return render(request, 'expenses/login.html', {
                'error': 'Invalid username or password'
            })

    else:
        return render(request, 'expenses/login.html')


def logout_page(request):
    return render(request, 'expenses/logout.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')


def show_books(request):
    allbooks = None
    current_user = None
    total_expense = 0
    if request.user.is_authenticated:
        current_user = request.user
        allbooks = AddBook.objects.filter(user=current_user)
    else:
        return redirect('login')

    for book in allbooks:
        total_expense += book.distribution_expense

    return render(request, 'expenses/show_books.html', {
        'allbooks': allbooks,
        'current_user': current_user,
        'total_expense': total_expense
    })


def book(request, id):
    addbook = None

    if request.user.is_authenticated:
        current_user = request.user
        addbook = AddBook.objects.get(user=current_user, pk=id)
    else:
        raise Http404

    return render(request, 'expenses/book.html', {'addbook': addbook})


def book_edit(request, id):
    addbook = None

    if request.user.is_authenticated:
        current_user = request.user
        addbook = AddBook.objects.get(user=current_user, pk=id)
    else:
        return redirect('login')

    if request.method == 'POST':
        addbook.title = request.POST.get('title')
        addbook.subtitle = request.POST.get('subtitle')
        addbook.authors = request.POST.get('authors')
        addbook.publisher = request.POST.get('publisher')
        addbook.published_date = request.POST.get('published_date')
        addbook.category = request.POST.get('category')
        addbook.distribution_expense = request.POST.get(
            'distribution_expense')
        addbook.save()

        return redirect('show_books')
    else:
        initial = {
            'title': addbook.title,
            'subtitle': addbook.subtitle,
            'authors': addbook.authors,
            'publisher': addbook.publisher,
            'published_date': addbook.published_date,
            'category': addbook.category,
            'distribution_expense': addbook.distribution_expense,
        }

    return render(request, 'expenses/book_edit.html', {'addbook': addbook, 'initial': initial})


def book_delete(request, id):
    addbook = None

    if request.user.is_authenticated:
        current_user = request.user
        addbook = AddBook.objects.get(user=current_user, pk=id)
    else:
        return redirect('login')

    if addbook is not None:
        addbook.delete()
        return redirect('show_books')

    return redirect('show_books')


def add_book(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            if (request.POST.get('title')
                    and request.POST.get('subtitle')
                    and request.POST.get('authors')
                    and request.POST.get('publisher')
                    and request.POST.get('published_date')
                    and request.POST.get('category')
                    and request.POST.get('distribution_expense')
                    ):
                addbook = AddBook(user=current_user)
                addbook.title = request.POST.get('title')
                addbook.subtitle = request.POST.get('subtitle')
                addbook.authors = request.POST.get('authors')
                addbook.publisher = request.POST.get('publisher')
                addbook.published_date = request.POST.get('published_date')
                addbook.category = request.POST.get('category')
                addbook.distribution_expense = request.POST.get(
                    'distribution_expense')
                addbook.save()
                return redirect('show_books')

    else:
        return redirect('login')

    return render(request, 'expenses/add_book.html', {})
