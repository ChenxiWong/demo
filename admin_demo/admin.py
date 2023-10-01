from django import forms
from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import Book


class BookForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError("Title must have at least 5 characters.")
        return title


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ['title', 'author', 'publication_date']
    search_fields = ['author']
    ordering = ['publication_date']

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        publication_date = cleaned_data.get('publication_date')
        if author and publication_date and author == 'John' and publication_date.year < 2000:
            raise ValidationError("John's books published before 2000 are not allowed.")


admin.site.register(Book, BookAdmin)
