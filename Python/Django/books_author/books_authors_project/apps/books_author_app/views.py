########## APP LEVEL views ############

from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     def __repr__(self):
#         return f"<Book object: {self.title}, description: {self.description}>"
        

# class Author(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     books = models.ManyToManyField(Book, related_name="authors")
#     notes = models.CharField(max_length=255, default="no notes")
#     def __repr__(self):
#         return f"<Author object: {self.first_name} {self.last_name}>"

def add_root(request):
    return redirect("/")

def index(request):
    context = {
        "all_the_books": Book.objects.all(),
    }
    return render(request, "books_author_app/index.html", context)


def add_book(request):
    if request.method == "GET":
       return redirect("/")
    if request.method == "POST":
        title = request.POST['book_title']
        description = request.POST['book_description']
        Book.objects.create(title=title, description=description)

        return redirect("/")


def add_author_to_book(request, book_id):
    if request.method == "Get":
       return redirect(f"books/{book_id}")
    if request.method == "POST":
        author_id = request.POST['author_id']
        Book.objects.get(id=book_id).authors.add(Author.objects.get(id=author_id))
        return redirect(f"/books/{book_id}")

def one_book(request, book_id):
    book = Book.objects.get(id=book_id)
    this_book_authors = book.authors.all()
    all_authors = Author.objects.all()
    other_authors = [author for author in all_authors if author not in this_book_authors]
    context = {
        "book":book,
        "other_authors": other_authors,
    }
    return render(request, "books_author_app/book.html", context)

def authors_page(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "books_author_app/author.html", context)

def add_author(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        first_name = request.POST['author_first_name']
        last_name = request.POST['author_last_name']
        notes = request.POST['author_notes']
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect("/authors")

def one_author(request, author_id):
    author = Author.objects.get(id=author_id)
    this_author_books = author.books.all()
    all_books = Book.objects.all()
    other_books = [book for book in all_books if book not in this_author_books]
    context = {
        "author": author,
        "other_books": other_books,
    }
    return render(request, "books_author_app/view_author.html", context)


def add_book_to_author(request, author_id):
    print("#####################")
    if request.method == "GET":
       return redirect(f"/author/{author_id}")
    if request.method == "POST":
        book_id = request.POST['book_id']
        Author.objects.get(id=author_id).books.add(Book.objects.get(id=book_id))
        return redirect(f"/authors/{author_id}")