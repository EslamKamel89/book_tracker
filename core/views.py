from typing import cast

from django.contrib.auth.decorators import login_required
from django.forms import BoundField
from django.http import HttpRequest
from django.shortcuts import render

from core.forms import BookForm
from core.models import Book, User


@login_required()
def index(request: HttpRequest):
    user = cast(User, request.user)
    form = BookForm(request.POST or None, user=user)
    if request.method == "POST":
        if not form.is_valid():
            response = render(request, "partials/form.html", {"form": form}, status=400)
            response["HX-Reswap"] = "outerHTML"
            response["HX-Retarget"] = "#book-form"
            return response
        name = form.cleaned_data["name"]
        genre = form.cleaned_data["genre"]
        book, _ = Book.objects.get_or_create(name=name, genre=genre)
        user.books.add(book)
        return render(request, "partials/row.html", {"book": book})

    books = user.books.all()

    return render(
        request,
        "index.html",
        {"books": books, "form": form},
    )
