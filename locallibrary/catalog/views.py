from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext
from django.utils.translation import gettext as _

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    trans = translate(language = 'vi')
    """View function for home page of site."""
    # trans = translate(language='vi')
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_books_contain_django = Book.objects.filter(title__contains='django').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'trans': trans,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_books_contain_django': num_books_contain_django,
        'num_authors': num_authors,
        'num_genres' : num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('Local Library')
    finally:
        activate(cur_language)
    return text