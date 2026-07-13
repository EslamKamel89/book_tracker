from django import forms

from core.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("name", "genre")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "e.g. Clean Code",
                }
            ),
            "genre": forms.Select(
                attrs={
                    "class": "select select-bordered w-full",
                }
            ),
        }
