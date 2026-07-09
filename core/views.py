from typing import cast

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

from core.forms import BookForm
from core.models import Book, User


@login_required()
def index(request: HttpRequest):
    user = request.user
    books = cast(User, user).books.all()
    form = BookForm()
    context = {"books": books, "form": form}
    return render(request, "index.html", context)
