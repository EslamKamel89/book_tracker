from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import Book, User


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
