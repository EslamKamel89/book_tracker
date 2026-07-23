from typing import Any

from django import forms

from core.models import Book, User


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user: User | None = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["name"].help_text = (
            "Enter a unique book title between 5 and 100 characters."
        )

    def clean_name(self):
        name = self.cleaned_data["name"]
        name = name.strip()
        if len(name) < 5:
            raise forms.ValidationError("Book name must contain at least 5 characters.")
        if len(name) > 100:
            raise forms.ValidationError("Book name cannot exceed 100 characters.")
        return name

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        genre = cleaned_data.get("genre")
        if not self.user:
            raise forms.ValidationError("Authenticated user is not known")
        if self.user.books.filter(name=name, genre=genre).exists():
            raise forms.ValidationError(
                f"You already have a {name} in your book list!!"
            )
        return cleaned_data

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
